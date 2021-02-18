#-*- coding:utf-8 -*-

import unittest
import re

from Tool.http_request import  Http_request

class KePadTestCase(unittest.TestCase):

    def setUp(self):
        self.login_url = "https://demo.fastadmin.net/index/user/login.html"
        self.index_url = "https://demo.fastadmin.net/index/user/index.html"
        self.req = Http_request()
        loginpage_response = self.req.send_request(self.login_url, methond="get")
        # 获取登录页面中表单中的token
        tokens = re.findall('<input type="hidden" name="__token__" value="(.*?)" />',
                           loginpage_response.text)
        self.token = tokens[0]
        #登录
        data = {"url": "https://demo.fastadmin.net/index/user/index.html",
                "account": "admin", "password": "123456", "keeplogin": "1", "__token__": self.token}
        login_response = self.req.send_request(self.login_url, data=data, methond="post")
        self.cookies = login_response.cookies

    def test_login_normal(self):#正常登录

        data = {"url": "https://demo.fastadmin.net/index/user/index.html",
                "account": "admin", "password": "123456", "keeplogin": "1", "__token__": self.token}
        login_response = self.req.send_request(self.login_url,data=data,methond="post",headers={'accept':'application/json'})
        try:
            self.assertIn("登录成功",login_response.text)
        except AssertionError as e:
            print("test_login_normal's error is {}".format(e))

    def test_login_error_password(self):  # 错误密码登录
        data = {"url": "https://demo.fastadmin.net/index/user/index.html",
                "account": "admin", "password": "12345678", "keeplogin": "1", "__token__": self.token}
        login_response = self.req.send_request(self.login_url, data=data, methond="post")
        try:
            self.assertIn("密码不正确",login_response.text)
        except AssertionError as e:
            print("test_login_error_password's error is {}".format(e))


    def test_login_index(self):#登录后访问个人中心
        index_response = self.req.send_request(self.index_url,methond="get",cookies=self.cookies)

    def tearDown(self):
        pass