# 文件名建议：tuple_student_scores_demo.py
# 学习主题：用 Python 元组 tuple 保存一名学生的基本信息和多科成绩

student = ("张三", 18, ("语文", 88), ("数学", 95), ("英语", 90))  # 创建一个元组，保存姓名、年龄，以及多个“科目+分数”的小元组

print("完整学生信息：", student)  # 打印整个元组，观察元组中保存的所有数据

name = student[0]  # 通过下标 0 取出元组中的第 1 个元素，也就是学生姓名
age = student[1]  # 通过下标 1 取出元组中的第 2 个元素，也就是学生年龄

chinese = student[2]  # 取出第 3 个元素，它本身也是一个元组，表示语文成绩信息
math = student[3]  # 取出第 4 个元素，它本身也是一个元组，表示数学成绩信息
english = student[4]  # 取出第 5 个元素，它本身也是一个元组，表示英语成绩信息

print("姓名：", name)  # 打印学生姓名，查看单个元素的取值结果
print("年龄：", age)  # 打印学生年龄，查看单个元素的取值结果

chinese_subject, chinese_score = chinese  # 元组解包，把语文元组中的科目名和分数分别赋值给两个变量
math_subject, math_score = math  # 元组解包，把数学元组中的科目名和分数分别赋值给两个变量
english_subject, english_score = english  # 元组解包，把英语元组中的科目名和分数分别赋值给两个变量

total_score = chinese_score + math_score + english_score  # 把三门课的分数相加，得到总分
average_score = total_score / 3  # 用总分除以科目数量 3，得到平均分

print("总分：", total_score)  # 打印学生三门课的总分
print("平均分：", average_score)  # 打印学生三门课的平均分

score_items = student[2:]  # 使用切片取出从第 3 个元素到最后的内容，也就是所有成绩小元组

for subject, score in score_items:  # 遍历成绩元组列表，并通过解包分别拿到科目名和分数
    print(subject, "成绩是：", score)  # 打印每一门科目的名称和对应分数

basic_info = (name, age)  # 创建一个新的元组，只保存学生的基础信息
contact_info = ("北京", "13800000000")  # 创建另一个新的元组，保存学生的城市和电话
full_info = basic_info + contact_info  # 使用加号拼接两个元组，生成一个新的元组

print("拼接后的信息：", full_info)  # 打印拼接后的新元组，观察元组相加的结果

print("元组长度：", len(student))  # 使用 len() 查看 student 元组中一共有多少个顶层元素
print("姓名出现次数：", student.count("张三"))  # 使用 count() 统计指定元素在元组中出现了几次
print("年龄所在下标：", student.index(18))  # 使用 index() 查找指定元素第一次出现的位置

try:  # 使用 try 尝试执行一段可能出错的代码
    student[0] = "李四"  # 尝试修改元组中的元素，这一行会报错，因为元组创建后不能直接修改
except TypeError as error:  # 捕获 TypeError 错误，说明刚才的修改操作不被允许
    print("元组不能直接修改：", error)  # 打印错误信息，理解元组“不可变”的特点

new_student = ("李四",) + student[1:]  # 如果想“修改”元组，通常是创建一个包含新内容的新元组

print("原来的学生元组：", student)  # 打印原元组，确认它没有被改变
print("新生成的学生元组：", new_student)  # 打印新元组，查看用新姓名生成后的结果
