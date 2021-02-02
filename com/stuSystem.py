import os

studentDBfile = r"studentInfo.txt"
def menu():
    print("=================================学生信息管理系统==================================")
    print("--------------------------------菜单---------------------------------------------")
    print("\t\t\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t\t\t5.学生成绩排名")
    print("\t\t\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t\t\t7.显示全部学生信息")
    print("\t\t\t\t\t\t\t\t0.退出系统")

def insert():
    print("insert")
    #创建学生集合
    student_list = []
    while True:
        id = input("请输入学生ID(如1001)：")
        if not id : #每个对象都有一个布尔值：数据默认是True，空为false 判断不是空字符串
            break
        name = input("请输入姓名：")
        if not name :
            break

        try:
            #int转换输入的内容，如果非数字则转换失败，走except
            englist = int(input("请输入英语成绩："))
            pythonlist = int(input("请输入python成绩："))
            javalist = int(input("请输入java成绩："))
        except:
            print("输入无效，不是整数类型，请重新输入")
            continue #继续循环方法里面的while true
        #将录入的学生信息录入到字典中
        student = {"id":id,"name":name,"englist":englist,"pythonlist":pythonlist,"javalist":javalist}
        #将学生信息的字典添加到集合中
        student_list.append(student)
        print(student_list)
        # save_studentInfo(studentDBfile,student_list)
        #数据添加成功后，询问是否继续添加学生信息
        answer = input("请问您是否继续添加N/Y")
        if answer =="y" or answer == "Y":
            # pass
            continue
        elif answer == "n" or answer == "N":
            #不再录入的时候，把列表的数据保存到文件中，并退出学生信息录入，进入菜单选择界面
            # save_studentInfo(studentDBfile, student_list) #功能可以实现，重新进入循环，之前存的数据清除
            break
    save_studentInfo(studentDBfile, student_list)

def save_studentInfo(filename,list):
    # if not os.path.exists(filename):
        # os.system(r"touch {}".format(path))
    try:
        f = open(filename, mode="a", encoding="utf-8")
    except:
        f = open(filename, mode="wt", encoding="utf-8")
    for item in list:
        f.write(str(item) + "\n")
    f.close()

"""
读取所有的学生信息，并返回id
"""
def delete_studentInfo(filename,id):
    student_dict = {}
    with open(filename,mode="rt",encoding="utf-8") as rf:
        readlines_str = rf.readlines()
        with open(filename,mode="wt",encoding="utf-8") as wf:
            for linestr in readlines_str:
                student_dict = dict(linestr) #每一行数据都是一个字典，字典显示学生的各种属性值
                # print(str(student_dict))
                if id in student_dict["id"]:
                    continue
                else:
                    wf.write(linestr)

    rf.close()

def read_studentInfo(filename):
    student_dict = {}
    with open(filename,mode="rt",encoding="utf-8") as rf:
        readlines_str = rf.readlines()
        for linestr in readlines_str:
            student_dict += dict(linestr) #每一行数据都是一个字典，字典显示学生的各种属性值
            print(str(student_dict))
    rf.close()

def search():
    print("search")
def delete():
    print("delete")
    input("请输入学生编号")
    delete_studentInfo(studentDBfile)
def modify():
    print("modify")
def sort():
    print("sort")
def total():
    print("total")
def show():
    print("show")
def exitSystem():
    print("exitSystem")

stu_dict01 = {"1":insert,"2":search,"3":delete,"4":modify,"5":sort,"6":total,"7":show,"0":exitSystem}

def main():

    while True:  #表示启动程序就一直运行
        menu()
        i = input("请选择：")

        if i in stu_dict01.keys():

            if i == "0":
                isexit = input("请确认是否退出，请选择N/Y")

                if isexit =="n" or isexit =="N":
                    # menu()
                    pass
                elif isexit =="y" or isexit =="Y":
                    break

            elif i == "3":
                isdelete = input("请确认是否删除，请选择N/Y")

                if isdelete  =="n" or isdelete =="N":
                    # menu()
                    pass
                elif isdelete =="y" or isdelete =="Y":
                    stu_dict01[i]()
                    break

            else:
                stu_dict01[i]()

        else:
            print("您选择错误，请重新选择")
            menu()

if __name__=="__main__":
    main()