class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 调库函数
        # 暴力
        # 分治
        # if not n:
        #     return 1
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # if n % 2:
        #     return x * self.myPow(x, n-1)
        # return self.myPow(x*x, n/2)

        # 非递归
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
