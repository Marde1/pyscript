# -*- coding：utf-8 -*-

import unittest
from WebTours.toursTestCase  import ToursTestCase
import HTMLTestRunnerNew

if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(ToursTestCase))

    with open("WebTouresResult.html",mode="wb") as resultFile:
        runner = HTMLTestRunnerNew.HTMLTestRunner(resultFile,
                                                  verbosity=2,
                                                  title="WebToures的测试报告",
                                                  description="主要是登录接口的功能自动化测试报告")
        runner.run(suite)
