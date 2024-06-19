# -*- coding: utf-8 -*-

import socket
import datetime as dt

# 创建一个 socket 应用，使用 IPV4 和 TCP 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定 ip 地址为本地回环地址，5201 端口
s.bind(("127.0.0.1", 5201))
# 要连接的服务端 ip 为本地回环地址，端口为 5200
s.connect(("127.0.0.1", 5200))
# 当 TCP 连接成功建立后，打印服务端返回的信息
print(s.recv(1024).decode("utf-8"), dt.datetime.now().strftime("%H:%M:%S:%f"))
# 向服务端发送信息
for data in [b"user1", b"user2", b"user3"]:
    s.send(data)
    # 打印服务端返回的信息
    print(s.recv(1024).decode("utf-8"), dt.datetime.now().strftime("%H:%M:%S:%f"))
# 想服务端发动断开连接的消息
s.send(b"exit")
# 客户端主动断开连接
s.close()
