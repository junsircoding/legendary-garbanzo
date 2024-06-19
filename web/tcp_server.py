# -*- coding: utf-8 -*-

import time
import datetime as dt
import socket
import threading

# 创建一个 socket 应用，同样使用 IPV4 和 TCP 协议
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# 绑定 ip 地址为本地回环地址，5200 端口
s.bind(("127.0.0.1", 5200))
# 开始监听请求，最多同时接受 5 个请求
s.listen(5)
print("Server is running ...%s" % dt.datetime.now().strftime("%H:%M:%S:%f"))

def tcplink(sock, addr):
    print("Get a new connection, ip:%s, port:%s, %s" % (addr[0], addr[1], dt.datetime.now().strftime("%H:%M:%S:%f")))
    sock.send(b"Hello!")
    while True:
        # 解码接收到的信息
        data = sock.recv(1024).decode("utf-8")
        time.sleep(1)
        # 如果接收到的信息是 exit，由服务端主动断开连接
        if data == "exit":
            print("Got exit message, close the connection, %s" % dt.datetime.now().strftime("%H:%M:%S:%f"))
            break
        print("Got a data: %s, %s" % (data, dt.datetime.now().strftime("%H:%M:%S:%f")))
        sock.send(("Hi, %s, I got you!" % data).encode("utf-8"))
    sock.close()
    print("Close a connection, ip:%s, port:%s, %s" % (addr[0], addr[1], dt.datetime.now().strftime("%H:%M:%S:%f")))

while True:
    # 收到一条请求，交由一个线程去处理
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

