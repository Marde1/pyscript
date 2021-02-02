class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("用户基本信息：姓名%s %s,年龄%s "% (self.first_name,self.last_name,self.age))

    def greet_user(self,content="海南人"):
        print(self.first_name,self.last_name,content)

if __name__=="__main__":
    user01 = User('tom','Smits','18')
    user01.describe_user()
    user01.greet_user('你好啊')