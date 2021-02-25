# -*- coding:utf-8 -*-
'''
    actor:Marde
    data:2021-2-24

'''

import unittest
import re

from Tool.http_request import Http_request #导入Http_request类

class TouresTestCase(unittest.TestCase):

    login_url = "http://localhost:1080/cgi-bin/login.pl"
    homePage_url = "http://localhost:1080//cgi-bin/nav.pl?in=home" #获取响应中form表单中的userSession值

    def test_login_normal(self): #正常登录
        req = Http_request()

        #访问home页面，通过正则提取响应的html表单中的userSession
        homePage_response = req.send_request(self.homePage_url,methond="get")
        print("----------------------------------")
        print(homePage_response.text)
        print("----------------------------------")
        user_session = re.findall('<input type="hidden" name="userSession" value="(.*?)"/>',homePage_response.text)

        print(user_session)

        data = {"userSession":user_session,
                "username":"test1",
                "password":"123456",
                "login.x":25,"login.y":3,
                "JSFormSubmit":"off"}
        print(data)
        login_response = req.send_request(self.login_url,methond="post",data=data)
        print(login_response.text)
        print(login_response.status_code)

    def test_login_errorPassword(self):#错误密码登录
        pass

    def test_login_emptyPassword(self):#密码为空登录
        pass