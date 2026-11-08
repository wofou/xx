# 文件名建议：json_study_demo.py  # 说明这个文件用于学习 Python 的 json 模块

import json  # 导入 Python 内置的 json 模块，用来处理 JSON 数据

student = {  # 创建一个 Python 字典，用来模拟一个学生的信息
    "name": "小明",  # 保存学生姓名
    "age": 18,  # 保存学生年龄
    "city": "上海",  # 保存学生所在城市
    "scores": {"语文": 88, "数学": 95, "英语": 91},  # 保存学生各科成绩，值里面又嵌套了一个字典
    "is_active": True,  # 保存学生是否在读，Python 里的 True 转成 JSON 后会变成 true
}  # 字典创建结束

print("原始 Python 字典：")  # 输出提示文字，说明下面打印的是 Python 字典
print(student)  # 打印原始字典数据

json_text = json.dumps(student, ensure_ascii=False, indent=4)  # 把 Python 字典转换成 JSON 字符串，并保留中文显示

print("\n字典转换成 JSON 字符串：")  # 输出提示文字，说明下面打印的是 JSON 字符串
print(json_text)  # 打印转换后的 JSON 字符串

new_student = json.loads(json_text)  # 把 JSON 字符串重新转换成 Python 字典

print("\nJSON 字符串转换回 Python 字典：")  # 输出提示文字，说明下面打印的是转换回来的字典
print(new_student)  # 打印转换后的 Python 字典
print("读取姓名：", new_student["name"])  # 通过字典的键读取学生姓名
print("读取数学成绩：", new_student["scores"]["数学"])  # 通过嵌套字典读取数学成绩

file_name = "student_info.json"  # 定义要保存的 JSON 文件名

with open(file_name, "w", encoding="utf-8") as file:  # 以写入模式打开文件，并使用 utf-8 编码保存中文
    json.dump(student, file, ensure_ascii=False, indent=4)  # 把 Python 字典直接写入 JSON 文件

print("\n已经把学生信息保存到文件：", file_name)  # 输出提示文字，说明 JSON 文件已经生成

with open(file_name, "r", encoding="utf-8") as file:  # 以读取模式打开刚才保存的 JSON 文件
    loaded_student = json.load(file)  # 从 JSON 文件中读取数据，并转换成 Python 字典

print("\n从 JSON 文件读取出来的数据：")  # 输出提示文字，说明下面打印的是文件中读取的数据
print(loaded_student)  # 打印从 JSON 文件读取出来的字典

for subject, score in loaded_student["scores"].items():  # 遍历学生成绩字典，subject 是科目，score 是分数
    print(subject, "成绩是", score)  # 输出每一门科目和对应成绩
