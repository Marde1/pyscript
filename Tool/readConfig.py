# -*- conding:utf-8 -*-

import configparser

class ReadConfig:

    def __init__(self,filename):
        self.filename = filename
        self.cf = configparser.RawConfigParser()
        self.cf.read(self.filename,encoding='utf-8')

    def get_value_str(self,section,option):
        """
        根据section和option获取value
        :param section:
        :param option:
        :return: value
        """
        value_str = self.cf.get(section,option)
        return value_str

    def get_value_dict(self,section):
        """
        根据section获取option，并遍历获取value，数据存入字典，并返回
        :param section:
        :return: key—value
        """
        opiton_list = self.cf.options(section)
        dict01 = {}
        for i in opiton_list:
            option_str = self.cf.get(section,i)
            dict01[i] = option_str
        return dict01

    def get_value_list(self):
        section_list = self.cf.sections()
        # print(section_list)
        list_value = []
        all_section_dict = {}
        for i in section_list:
            print(self.get_value_dict(i))
            # print(i)
            # opiton_list = self.cf.options(i)
            # print(i)
            # print(opiton_list)
            # value_dict = {}
            # for j in opiton_list:
            #     print(j)
            #     print(i,j)
            #     value_dict[i] = self.cf.get(i, j)
            # print(value_dict)
            # section_dict[i] = dict01
            # print(section_dict)
        # list_value.append(section_list)
        # print(list_value)

if __name__ == "__main__":
    rc = ReadConfig("F:\demo\config.ini")
    print(rc.get_value_str("formatter_form01","format"))
    # print(rc.get_value_dict("logger_root"))
    rc.get_value_list()
