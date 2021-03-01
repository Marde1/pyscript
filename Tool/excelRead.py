# -*- coding:utf-8 -*-

import openpyxl

class ExcelRead():

    def __init__(self,filename,sheetname):
        self.wb = openpyxl.load_workbook(filename)
        self.sheet = self.wb[sheetname]

    def readData(self):
        maxrow_num = self.sheet.max_row
        maxcolumn_num = self.sheet.max_column
        # print("最大行：",maxrow_num)
        # print("最大列：",maxcolumn_num)
        data_dict = {}
        data_list =[]
        if(maxrow_num>0 and maxcolumn_num>0):
            for i in range(2,maxrow_num+1): #行
                for j in range(1,maxcolumn_num+1):#列
                    # print(i,j)
                    # print(self.sheet.cell(1,j).value)
                    # print(self.sheet.cell(i,j).value)
                    data_dict[self.sheet.cell(1,j).value] = self.sheet.cell(i,j).value
                # print(data_dict)
                data_list.append(data_dict)
                data_dict = {} #数据存入列表后清空字典，以便后面的数据存入
        return data_list

# if __name__ == "__main__":
#     excel = ExcelRead(r"..\WebTours\webTour_data.xlsx","data")
#     list01 = excel.readData()
#     print(list01)