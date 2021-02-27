# -*- coding:utf-8 -*-

import openpyxl

# class ExcelRead():

    # def __init__(self,filename,sheetname):
    #     self.wb = load_workbook(filename)
        # self.sheet = self.wb[sheetname]

    # def readData(self):
        # maxrow_num = self.sheet.max_row
        # maxcloumn_num = self.max_column
        # data_dict = {}
        # data_list =[]
        # if(maxrow_num>0 and maxcloumn_num>0):
        #     for i in (2,maxrow_num):
        #         for j in maxcloumn_num:
        #             data_dict[j] = self.sheet.cell[i,j].value
        #         data_list.append(data_dict)
        # return data_list
        # return self.max_column
if __name__ == "__main__":
    # excel = ExcelRead(r"C:\Users\hp\Desktop\pyscript\WebTours\webTour_data.xlsx","data")
    # print(excel.readData())

    wb = openpyxl.loadworkbook(r"C:\Users\hp\Desktop\pyscript\WebTours\webTour_data.xlsx")
    # sheet = wb["data"]