# -*- coding:utf-8 -*-

import xlrd

class ExcelRead:

    def __init__(self,worksheet):
        self.worksheet = worksheet


if __name__ == "__main__":
    # table = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\业务单元拓扑关系+部署信息表v1.0.xlsx") #打开excel
    # sheet = table.sheet_by_name("部署beat所需信息") #进入到某sheet页
    # # sheet.row_values()
    # # sheet.col_values()
    # print(dir(sheet)) #打印sheet的所有方法
    # print(sheet.nrows) #打印该sheet页有效行数
    # print(sheet.ncols) #打印该sheet页有效列数
    # print(sheet.cell(1,0).value) #打印该sheet页第二行，第一列的单元格cell的值
    # print(sheet.row_values(0)) #打印第一行的所有值，返回list
    # print(sheet.row_values(1)) #打印第二行的所有值，返回list
    # print(dict(zip(sheet.row_values(0),sheet.row_values(1)))) #第一行和第二行的数据组合成字典，可以用这个组合成发送请求的json数据
    # # （将数据和标题组装成字典，使数据更清晰）
    #
    # worksheets = table.sheet_names() #获取表的所有sheet的名称，返回list
    # print("sheets名：",worksheets)
    pass
