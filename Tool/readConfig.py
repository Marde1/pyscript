# -*- conding:utf-8 -*-

import configparser

class ReadConfig:

    def __init__(self,filename):
        self.filename = filename
        self.cf = configparser.ConfigParser()
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
            dict01[i] = self.cf.get(section,i)
        return dict01

    def get_value_list(self):
        section_list = self.cf.sections()
        print(section_list)
        list_value = []
        section_dict = {}
        for i in section_list:
            print(i)
            opiton_list = self.cf.options(i)
            dict01 = {}
            for i in opiton_list:
                dict01[i] = self.cf.get(i, i)
            # section_dict[i] = dict01
            # print(section_dict)
        # list_value.append(section_list)
        # print(list_value)

if __name__ == "__main__":
    rc = ReadConfig("F:\demo\config.ini")
    print(rc.get_value_str("loggers","keys"))
    print(rc.get_value_dict("logger_root"))
    rc.get_value_list()
