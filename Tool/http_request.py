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

    def send_request(self,url,params=None,data=None,headers=None,methond="get",cookie=None,verify=False):

        if methond.lower()=="get":
            response = self.res.get(url,params=params,headers=self.headers)
        else:
            response = self.res.post(url,data=data,headers=headers,cookies=cookie,verify=verify)
        return response


