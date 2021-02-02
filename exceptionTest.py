# -*- coding:utf-8 -*-

class Test:

    def str_int(self,str):

        try:
            return int(str)
        except ValueError:
            print("%s字符串无法成功转换为int类型" % str)

t = Test()
print(t.str_int("111"))
print(t.str_int("abc"))

print(16 ** 0.5)