# -*- coding:utf-8 -*-

#实现计算求最大公约数和最小公倍数的函数
"""
求最大公约数算法:

整数A对整数B进行取整, 余数用整数C来表示 举例: C = A % B

如果C等于0,则C就是整数A和整数B的最大公约数

如果C不等于0, 将B赋值给A, 将C赋值给B ,然后进行 1, 2 两步,直到余数为0, 则可以得知最大公约数
"""
def gcd(x, y):
    """求最大公约数"""
    if x > y:
        (x, y) = (y, x)
    else:
        (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print(x)
            print(factor)
            # return factor

gcd(32,88)