# -*- coding：utf-8 -*-

import unittest
from WebTours.toursTestCase  import ToursTestCase #类名
import HTMLTestRunnerNew
# from Tool.excelRead import ExcelRead

testdata = [{"url":"http://localhost:1080/cgi-bin/login.pl","data":{"userSession":None,"username":"test1","password":"123456","login.x":25,"login.y":3,"login":"Login","JSFormSubmit":"off"},"expected":"login.pl?intro=true","method":"post"},
                {"url": "http://localhost:1080/cgi-bin/login.pl","data": {"userSession": None, "username": "test1", "password": "123457", "login.x": 25,"login.y": 3, "login": "Login", "JSFormSubmit": "off"}, "expected": "error.pl?error=badPassword","method":"post"},
                {"url": "http://localhost:1080/cgi-bin/login.pl","data": {"userSession": None, "username": "test11", "password": "123456", "login.x": 25,"login.y": 3, "login": "Login", "JSFormSubmit": "off"},"expected": "error.pl?error=badPassword","method":"post"}
                ]

if __name__ == "__main__":
    excel = ExcelRead("webTour_data.xlsx","data")
    testdata = excel.readData()


    suite = unittest.TestSuite()
    #通过初始化函数传参
    for item in testdata:
        #通过实例的方式加载用例
        suite.addTest(ToursTestCase("test_api",item["url"],item["data"],item["expected"],item["method"]))

    with open("WebToursResult.html",mode="wb") as resultFile:
        runner = HTMLTestRunnerNew.HTMLTestRunner(resultFile,
                                                  verbosity=2,
                                                  title="WebTours的测试报告",
                                                  description="主要是登录接口的功能自动化测试报告")
        runner.run(suite)
