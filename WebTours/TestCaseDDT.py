# -*- coding:utf-8 -*-

from ddt import ddt,data,unpack
import unittest
from Tool.excelRead import ExcelRead
import re
from Tool.http_request import Http_request #导入Http_request类

userSession = None

data_sheet = ExcelRead("webTour_data.xlsx","data");
testdata = data_sheet.readData()

@ddt #装饰测试类
class TestCaseDDT(unittest.TestCase):

    welcomePage_url = "http://localhost:1080/cgi-bin/welcome.pl?signOff=true"
    homePage_url = "http://localhost:1080/cgi-bin/nav.pl?in=home"  # 获取响应中form表单中的userSession值
    req = Http_request()

    def setUp(self):
        global userSession
        welcomePage_response = self.req.send_request(self.welcomePage_url, method="get")
        welcome_cookies = welcomePage_response.cookies
        homePage_response = self.req.send_request(self.homePage_url, method="get", cookies=welcome_cookies)
        userSession = re.findall('<input type="hidden" name="userSession" value="(.*?)"/>', homePage_response.text)
        # self.data = eval(data)
        # self.data["userSession"] = userSession[0]  # 从响应中获取的值再塞入到data数据中

    @data(*testdata) #方法装饰器
    # @unpack #脱外套
    def test_api(self,dict_data):
        # dict_data = eval(data)
        print()
        data = eval(dict_data["data"])
        data["userSession"]= userSession[0]
        print("测试用例编号:{}".format(dict_data["testcase_id"]))
        print("测试功能模块:{}".format(dict_data["function_module"]))
        print("测试用例标题:{}".format(dict_data["testcase_title"]))
        print("测试数据url:{}".format(dict_data["url"]))
        print("测试数据data:{}".format(dict_data["function_module"]))
        print("测试数据method:{}".format(dict_data["method"]))
        print("预期结果:{}".format(dict_data["expected"]))
        login_response = self.req.send_request(dict_data["url"], method=dict_data["method"], data=data)
        # print(login_response.text)
        login_list = re.findall('<frame src="(.*?)" name="info"', login_response.text)
        login_str = login_list[0]
        # print(login_list[0])
        print("实际结果:", login_str)
        try:
            self.assertEqual(login_str, dict_data["expected"],msg="fail")
            data_sheet.updateResultData(dict_data["testcase_id"]+1,"pass")

        except AssertionError as e:
            print("出现异常：", e)
            raise e

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

