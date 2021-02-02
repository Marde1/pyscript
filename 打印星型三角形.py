# -*- coding:utf-8 -*-
#三角形
def get_triangle(max):
    for i in range(max):
        if i<= max/2 :
            print("*" * i)
        else:
            print("*" *(max-i))



get_triangle(20)