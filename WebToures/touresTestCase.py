# -*- coding:utf-8 -*-
'''
    actor:Marde
    data:2021-2-24

'''

import unittest

from Tool.http_request import Http_request #导入Http_request类

class touresTestCase(unittest.TestCase):

    login_url = "http://localhost:1080/cgi-bin/login.pl"

    def test_login_normal(self): #正常登录
        data = {"userSession":None,"username":"test1","password":"123456","login.x":25,"login.y":3,"JSFormSubmit":"off"}
        req = Http_request()
        req.send_request(self.login_url,methond="post")

    def test_login_errorPassword(self):#错误密码登录
        pass

    def test_login_emptyPassword(self):#密码为空登录
        pass