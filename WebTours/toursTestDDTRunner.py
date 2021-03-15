# -*- conding:utf-8 -*-

import unittest
import HTMLTestRunnerNew
from WebTours.TestCaseDDT import TestCaseDDT

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCaseDDT))
    with open("WebToursResult.html",mode="wb") as file:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                verbosity=2,
                                                title="WebTours登录接口测试DDT",
                                                description=None,
                                                tester=None)
        runner.run(suite)

