# -*- coding:utf-8 -*-

import requests
import re

#不带参数的get请求
# url = "http://www.baidu.com"
#
# response = requests.get(url)
#
# print(response.status_code)
# print(response)
# print(response.headers)
# print(response.headers["Content-Type"])
# print(response.encoding)
# print(response.text)
# print(response.history)

"""
带参数的get请求
(1)参数直接放到url变量中
"""
# url = "http://www.baidu.com/?name=ketty"
# response = requests.get(url)
# print(response.text)
# print(response.url)
"""
(2)参数放到变量里，字典类型
"""
# url = "http://www.baidu.com"
# params = {"name":"ketty"} #变量支持字典、list和元组
# response = requests.get(url,params)
# print(response.text)
# print(response.url)

"""
 利用图灵聊天接口（GET） http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好，结合Python的input编写一个
机器人聊天室
"""


# def get_tuling(str):
#     url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe"
#     params = {"info":str}
#     response = requests.get(url,params)
#     print(response.text)
#     dict01 = json.loads(response.text)
#     print(dict01["text"])


# while True:
#     str = input("你好，请输入：")
#     if str:
#         get_tuling(str)

# def post_request(url,data):
#     response = requests.post(url,data)
#     print(response.text)

if __name__ == "__main__":
    # url = "http://openapi.tuling123.com/openapi/api/v2"
    # data =  {
    #         "reqType":0,
    #         "perception": {
    #         "inputText": {
    #         "text": "附近的美食"
    #         },
    #         "inputImage": {
    #             "url": "imageUrl"
    #             },
    #         "selfInfo": {
    #             "location": {
    #                 "city": "上海",
    #                 "province": "上海",
    #                 "street": "南京东路"
    #                 }
    #             }
    #         },
    #         "userInfo": {
    #             "apiKey": "ec961279f453459b9248f0aeb6600bbe",
    #             "userId": "206379"
    #         }
    #     }
    # post_request(url,data)

    # res_text = '{"name": "\u5f20\u4e09", "password": "123456", "male": true, "money": null}'  # JSON文本格式的响应信息
    # res_dict = json.loads(res_text)  # 转化为字典
    # print(res_dict['name'])  # 方便获取其中的参数值
    # print(res_dict["male"])
    # data = '{"name": "\u5f20\u4e09", "password": "123456", "male": true, "money": null}'
    # dict_data = json.loads(data)
    # print(dict_data)
    # str_data = json.dumps(dict_data,indent=2)
    # print(str_data)

    res = requests.session()
    url = "https://demo.fastadmin.net/index/user/login.html"
    login_res = res.get(url)
    token = re.findall('<input type="hidden" name="__token__" value="(.*?)" />',login_res.text)
    # print(token[0])
    data = {"url":"https://demo.fastadmin.net/index/user/index.html",
            "account":"admin","password":"123456","keeplogin":"1","__token__":token[0]}
    response = res.post(url,data)
    index_Url = "https://demo.fastadmin.net/index/user/index.html"
    response = res.get(url=index_Url)
    print(response.text)
    res.close()