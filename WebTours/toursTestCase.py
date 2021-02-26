# -*- coding:utf-8 -*-
'''
    actor:Marde
    data:2021-2-24

'''

import unittest
import re

from Tool.http_request import Http_request #导入Http_request类

class ToursTestCase(unittest.TestCase):

    welcomePage_url = "http://localhost:1080/cgi-bin/welcome.pl?signOff=true"
    homePage_url = "http://localhost:1080/cgi-bin/nav.pl?in=home" #获取响应中form表单中的userSession值
    login_url = "http://localhost:1080/cgi-bin/login.pl"

    def __init__(self,methodName,url,data,method):
        super(ToursTestCase,self).__init__(methodName)
        self.req = Http_request()

    def setUp(self):
        pass

    def test_login_normal(self): #正常登录
        self.req = Http_request()
        welcomePage_response = self.req.send_request(self.welcomePage_url,methond="get")
        welcomePage_cookie = welcomePage_response.cookies
        #访问home页面，通过正则提取响应的html表单中的userSession
        homePage_response = self.req.send_request(self.homePage_url,methond="get",cookies=welcomePage_cookie)
        user_session = re.findall('<input type="hidden" name="userSession" value="(.*?)"/>',homePage_response.text)

        data = {"userSession":user_session,
                "username":"test1",
                "password":"123456",
                "login.x":25,
                "login.y":3,
                "login":"Login",
                "JSFormSubmit":"off"}

        login_response = self.req.send_request(self.login_url,methond="post",data=data)
        login_list = re.findall('<frame src="(.*?)" name="navbar"',login_response.text)
        login_str = login_list[0]
        try:
            self.assertEqual(login_str,"nav.pl?page=menu&in=home")
        except AssertionError as e:
            print("出现异常：",e)
            raise Exception("抛出异常",e)


    def test_login_errorPassword(self):#错误密码登录
        pass

    def test_login_emptyPassword(self):#密码为空登录
        pass

    def tearDown(self):
        pass