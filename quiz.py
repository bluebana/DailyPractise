"""
作者：YuanMengna
日期：2021年12月18日
"""
import time
student=[]
class Studentinfo():
    """学生的信息档案"""
    def __init__(self,num,name,sex,birthday):
        self.num=num
        self.name=name
        self.sex=sex
        self.birthday=birthday

class Options():
    """用户输入数字进行操作"""
    def __init__(self):
        pass

    def operate(self,operatenum):
        operatenum = x
        if operatenum==1:
            num = input("请输入学生学号：")
            b = []
            for i in student:
                b.append(i.num)
            if num in b:
                print("请不要重复输入！")
            else:
                name = input("请输入学生姓名：")
                sex = input("请输入学生性别：")
                birthday = input("请输入学生生日：")
                aa = Studentinfo(num, name, sex, birthday)
                student.append(aa)
        elif operatenum==2:
            delnum = input("请输入需要删除的学生的学号：")
            b = []
            for i in student:
                b.append(i.num)
            if delnum not in b:
                print("该学生不存在！请输入正确的学号！")
            for i in student:
                if i.num == delnum:
                    student.remove(i)
        elif operatenum==3:
            chnum = input("请输入需要修改的学生的学号：")
            b = []
            for i in student:
                b.append(i.num)
            if chnum not in b:
                print("该学生不存在！请输入正确的学号！")
            for i in student:
                if i.num == chnum:
                    num = input("请输入学生学号：")
                    name = input("请输入学生姓名：")
                    sex = input("请输入学生性别：")
                    birthday = input("请输入学生生日：")
                    bb = Studentinfo(num, name, sex, birthday)
                    c = student.index(i)
                    student[c] = bb
        elif operatenum==4:
            print("-----------------以下是学生信息------------------")
            print("学号" + "\t" + "姓名" + "\t" + "性别" + "\t" + "生日")
            for i in student:
                print(i.num + "\t" + i.name + "\t" + i.sex + "\t" + i.birthday)
        elif operatenum==5:
            print("再见！！！")
        else:
            print("请输入正确的操作数字！")

while True:
    print("------------------welcome to the student management system-------------------")
    print("""
    1.添加学生
    2.删除学生
    3.修改学生
    4.查看学生
    5.退出
    """)
    x=int(input("请输入您的选择："))
    cc=Options()
    cc.operate(x)
    time.sleep(1)
    if x==5:
        break