


class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名: {self.name} | 语文:{self.chinese} | 数学: {self.math} | 英语: {self.english} | 总分: {self.chinese + self.math +self.english}"
        
    def update_score(self, chinese=None, english=None, math=None):
        if chinese is not None:
            self.chinese = chinese
        if english is not None:
            self.english = english
        if math is not None:
            self.math = math


class edumanagemen:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input("请输入学生名字: ")

        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在，添加失败！")
                return
        
        chinese = int(input("请输入学生语文成绩: "))
        math = int(input("请输入学生数学成绩: "))
        english = int(input("请输入学生英语成绩: "))


        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功~")
        else:
            print("各科成绩必须得在 0-100 之间 ！")

        
    def update_student(self):
         name = input("请输入要修改的学生姓名: ")

         for s in self.student_list:
             if s.name == name:
                 print(f"当前成绩: {s}")

                 chinese = int(input("请输入修改后的语文成绩: "))
                 math = int(input("请输入修改后的数学成绩: "))
                 english = int(input("请输入修改后的英语成绩: "))

                 if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                     s.update_score(chinese,math,english)
                     print("成绩修改成功后 ~")
                     print(f"修改后的成绩: {s}")
                     return
                 else:
                     print("各科成绩必须在 0-100 之间 ！")
                     return
         print("未找到该学生，修改失败！")    

    def delete_student(self):
        name = input("请输入要删除的学生名字: ")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功~")
                return
        print("未找到该学生，删除失败 ！")

    def query_student(self):
        name = input("请输入要查询的学生名字: ")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("未找到该学生！")

    def list_student(self):
        for s in self.student_list:
            print(s)
    
    def run(self):
        print(f"欢迎使用教务管理系统 v{edumanagemen.system_version}")


        while True:
            print()
            print("# 1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 #")
            print()
            choice = input("请输入要执行的操作，输入1-6:   ")
            print()
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.list_student()
                case "6":
                    print("bye ~")
                    break
                case _:
                    print("输入错误，请选择1-6之间的菜单功能！")


if __name__ == '__main__':
    edu_management = edumanagemen()
    edu_management.run()