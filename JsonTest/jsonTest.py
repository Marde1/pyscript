# -*- coding:utf-8 -*-

import json
import tkinter
import re

class Window_Gui:

    def __init__(self,init_window):
        self.main_window = init_window

    def set_mainWindow(self):

        self.main_window.title("JSON格式转换")

        # main_window.geometry("900x900")  #这里的乘号是英文字母x,不是*
        # main_window.resizable(0,0)  # 不允许 改变 窗口的宽和高
        x,y = self.main_window.maxsize()
        self.main_window.geometry("%dx%d" % (x,y)) #窗口最大化

        self.main_window_Text1 = tkinter.Text(self.main_window,bd=2,undo=True)
        self.main_window_Text1.pack(side=tkinter.TOP,expand=tkinter.YES,fill=tkinter.BOTH)#fill=tkinter.BOTH 全部填充  expand=tkinter.YES允许扩展
        self.main_window_Text1_Scrollbar = tkinter.Scrollbar(self.main_window_Text1)
        self.main_window_Text1.config(yscrollcommand=self.main_window_Text1_Scrollbar.set)
        self.main_window_Text1_Scrollbar.config(command=self.main_window_Text1.yview)
        self.main_window_Text1_Scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.main_window_Button = tkinter.Button(self.main_window,bd=2,text="转换",command=self.click_button)
        self.main_window_Button.pack()



        self.main_window_Text2 = tkinter.Text(self.main_window,bd=2,undo=True)
        self.main_window_Text2.pack(expand=tkinter.YES,fill=tkinter.BOTH)
        self.main_window_Text2_Scrollbar = tkinter.Scrollbar(self.main_window_Text2)
        self.main_window_Text2.config(yscrollcommand=self.main_window_Text2_Scrollbar.set)
        self.main_window_Text2_Scrollbar.config(command=self.main_window_Text2.yview)
        self.main_window_Text2_Scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)




    def get_text1_info(self):
        str = self.main_window_Text1.get("0.0","end")
        return str

    #功能函数
    def click_button(self):
        str = self.get_text1_info()

        if str:
            data = self.json_transfor(str)
            self.main_window_Text2.delete("1.0","end") #先删除text2里面的内容
            self.main_window_Text2.insert("0.0",data)


    def json_transfor(self,str):

        try:#当原数据转换为字典或者转换成json格式报错，直接显示原数据
            dict01 = json.loads(str)
            data = json.dumps(dict01, sort_keys=True, indent=2, separators=(', ', ': '), skipkeys=True,ensure_ascii=False)
        except Exception:
            data = str
            # data = re.sub("^{","{\n",str,0)
            # data = re.sub("}", "}\n", data, 0)
            # data = re.sub("\[", "[\n", data, 0)
            # data = re.sub("]", "]\n", data, 0)
            # data = re.sub(",", ",\n", data, 0)
            print(data)

        return data

def main():
    init_window = tkinter.Tk() #实例化一个父窗口
    w = Window_Gui(init_window)
    w.set_mainWindow() #设置窗口属性
    init_window.mainloop()  # 运行窗口，创建GUI根窗体




if __name__ == "__main__":
    main()

