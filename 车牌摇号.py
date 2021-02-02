# -*- coding:utf-8 -*-
"""
需求：
    1.允许用户最多选3次
    2.每次放出20个车牌供用户选择
    3.京[A-Z]-[XXXXXX]，可以是数字和字母的组合
"""
import random
import string
"""
    创建车牌类
    可以进行摇号，选择车牌，然后得到车牌
"""
class LicensePlate:

    #车牌
    def __init__(self):
        pass

    def get_licensePlate(self):
        count = 0
        while count <4:
            for i in range(20):
                n1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                # print(n1)
                count +=1
                n2 = random.sample("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",6)

                print(n1+str(n2))


if __name__== "__main__":
    l1 = LicensePlate()
    l1.get_licensePlate()
    print(random.choice("abcdefg"))