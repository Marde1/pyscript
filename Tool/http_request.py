# -*- coding:utf-8 -*-

import requests

#封装requests
class Http_request:

    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
        self.res = requests.session()  # 实例化一个会话实例

    def __del__(self):
        """关闭会话"""
        self.res.close()

    def send_request(self,url,params=None,data=None,headers=None,methond="get",cookies=None,verify=False):

        if methond.lower()=="get":
            response = self.res.get(url,params=params,headers=self.headers)
        else:
            response = self.res.post(url,data=data,headers=headers,cookies=cookies,verify=verify)
        return response

if __name__ == "__main__":
    res = Http_request() #实例化一个会话
    loginpage_url = "https://demo.fastadmin.net/index/user/login.html"
    loginpage_response = res.send_request(loginpage_url,methond="get") #会话访问登录页面
    import re
    token = re.findall('<input type="hidden" name="__token__" value="(.*?)" />',loginpage_response.text) #获取登录页面中表单中的token
    print(token)
    data = {"url": "https://demo.fastadmin.net/index/user/index.html",
            "account": "admin", "password": "123456", "keeplogin": "1", "__token__": token[0]}
    login_response = res.send_request(loginpage_url,methond="post",data=data) #会话 登录
    login_cookies = login_response.cookies # 获取登录后的cookies,后面的登录后页面访问需要
    print(login_response)
    index_url = "https://demo.fastadmin.net/index/user/index.html"
    index_response = res.send_request(index_url,cookies=login_cookies) #传入登录后获取的cookies，访问首页
    print(index_response.text)

