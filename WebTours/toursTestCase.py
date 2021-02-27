# -*- coding:utf-8 -*-
'''
    actor:Marde
    data:2021-2-24

'''

import unittest
import re

from Tool.http_request import Http_request #导入Http_request类

userSession = None

class ToursTestCase(unittest.TestCase):

    welcomePage_url = "http://localhost:1080/cgi-bin/welcome.pl?signOff=true"
    homePage_url = "http://localhost:1080/cgi-bin/nav.pl?in=home" #获取响应中form表单中的userSession值

    # login_url = "http://localhost:1080/cgi-bin/login.pl" #登录页面


    def __init__(self,methodName,url,data,expected,method):
        super(ToursTestCase,self).__init__(methodName)
        self.req = Http_request()
        self.url = url
        self.data = data
        self.expected = expected
        self.method = method

    def setUp(self):#每个测试用例的前置条件
        global userSession
        welcomePage_response = self.req.send_request(self.welcomePage_url, method="get")
        welcome_cookies = welcomePage_response.cookies
        homePage_response = self.req.send_request(self.homePage_url, method="get", cookies=welcome_cookies)
        userSession = re.findall('<input type="hidden" name="userSession" value="(.*?)"/>', homePage_response.text)
        # data_dict = eval(self.data)
        self.data["userSession"] = userSession #从响应中获取的值再塞入到data数据中

    def test_api(self): #正常登录
        #访问home页面，通过正则提取响应的html表单中的userSession
        # print(userSession)
        print("测试数据url：{}".format(self.url))
        print("测试数据data：{}".format(self.data))
        print("测试数据expected：{}".format(self.expected))
        print("测试数据method：{}".format(self.method))
        login_response = self.req.send_request(self.url,method=self.method,data=self.data)
        print(login_response.text)
        login_list = re.findall('<frame src="(.*?)" name="info"',login_response.text)
        login_str = login_list[0]
        print(login_list[0])
        try:
            self.assertEqual(login_str,self.expected)
        except AssertionError as e:
            print("出现异常：",e)
            raise e


    # def test_login_errorPassword(self):#错误密码登录
    #     pass
    #
    # def test_login_emptyPassword(self):#密码为空登录
    #     pass

    def tearDown(self):
        pass