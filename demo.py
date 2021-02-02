# import time
import random


import os,sys

def make_code(n):
    res = ''
    for i in range(n):
        # print(i)
        s1 = chr(random.randint(65,90))  #随机选择A-Z 26个字母
        s2 = str(random.randint(0,9)) #随机选择0-9 10个阿拉伯数字
        res+= random.choice([s1,s2])
    return res

if __name__ == "__main__":
    print(make_code(5))

    possible_topdir = os.path.normcase(os.path.join(
        os.path.abspath(__file__),
        os.pardir,
        os.pardir,
        os.pardir
    ))
    sys.path.insert(0,possible_topdir)
    print(sys.path)
    print(os.pardir)




























