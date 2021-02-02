# -*- coding:utf-8 -*-

import pymysql

class MysqlConnection():

    def __init__(self,conn):
        self.conn = conn #连接数据库对象属性
        self.cur = self.conn.cursor() #连接游标对象属性

    def __del__(self):
        # print("关闭游标和数据库连接")
        self.cur.close() #关闭游标
        self.conn.close() #关闭数据库连接

    def query_data(self,str): #查询
        self.cur.execute(str)
        return self.cur.fetchall()

    def operate_data(self,str):#增 删 改都可以
        try:
            status = self.cur.execute(str)
            if status!=0:
                print("success") #脚本执行成功，数据操作成功
                return True
                self.conn.commit() #提交
            else:
                print("fail")
                return True #脚本执行成功，数据操作失败
        except Exception as e:
            self.conn.rollback() #回滚
            print(str(e))
            return False #脚本执行报错



if __name__ == "__main__":
    conn = pymysql.connect("localhost","root","","stuinfo") # pymysql.connect(ip,username,password,数据库)实例化一个数据库连接
    myConn = MysqlConnection(conn) # 实例化对象传到类MysqlConnection中初始化
    # sql_str = "select * from student where s_name = {0}"
    a = myConn.query_data("select * from student where s_name like {0} ".format("'钱%'"))
    print(a)
    print(myConn.operate_data("update student set s_name= '赵雷' where s_name = '赵雷1'"))
    print(myConn.operate_data("delete from student where s_name = '赵雷'"))
    print(myConn.operate_data("INSERT INTO `stuinfo`.`student` (`s_id`, `s_name`, `s_birth`, `s_sex`) VALUES ('01', '赵雷1', '1990-01-01', '男')"))