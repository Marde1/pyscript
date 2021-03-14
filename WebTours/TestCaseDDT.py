# -*- coding:utf-8 -*-

from ddt import ddt,data,unpack
import unittest

@ddt #装饰测试类
class TestCaseDDT(unittest.TestCase):

    def __init__(self,testdata):
        super(self,TestCaseDDT).__init__()
        self.testdata = testdata

    def setUp(self):
        pass

    @data(1) #方法装饰器
    def test_api(self,i):
        print(i)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

