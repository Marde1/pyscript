# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunnerNew
from TestCase.TestkeTangPadCase import KePadTestCase

if __name__ == '__main__':

    #通过loader来加载用例
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(KePadTestCase))

    #执行
    with open("login_result.html",mode="wb") as file:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="登录的测试报告",
                                            description=None)
        runner.run(suite)