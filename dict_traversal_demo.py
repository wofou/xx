# 文件名建议：dict_traversal_demo.py  # 说明这个文件用于学习 Python 字典和字典遍历

student_scores = {"小明": 88, "小红": 95, "小刚": 76}  # 创建一个字典，键是学生姓名，值是对应分数

print("原始字典：", student_scores)  # 输出整个字典，方便先看到完整数据

print("\n方法1：直接遍历字典，默认拿到的是键")  # 输出提示文字，说明下面演示第一种遍历方法
for name in student_scores:  # 遍历字典本身，循环变量 name 每次拿到一个键
    print("学生姓名：", name)  # 输出当前遍历到的键，也就是学生姓名

print("\n方法2：使用 keys() 遍历所有键")  # 输出提示文字，说明下面演示 keys() 方法
for name in student_scores.keys():  # 使用 keys() 获取字典里所有的键，再逐个遍历
    print("学生姓名：", name)  # 输出当前遍历到的学生姓名

print("\n方法3：使用 values() 遍历所有值")  # 输出提示文字，说明下面演示 values() 方法
for score in student_scores.values():  # 使用 values() 获取字典里所有的值，再逐个遍历
    print("分数：", score)  # 输出当前遍历到的分数

print("\n方法4：使用 items() 同时遍历键和值")  # 输出提示文字，说明下面演示 items() 方法
for name, score in student_scores.items():  # 使用 items() 同时获取每一组键和值
    print(name, "的分数是", score)  # 输出当前学生姓名和对应分数

print("\n方法5：遍历时顺便统计序号")  # 输出提示文字，说明下面演示 enumerate() 和 items() 搭配使用
for index, (name, score) in enumerate(student_scores.items(), start=1):  # 给每一组键值对加上从 1 开始的序号
    print("第", index, "位学生：", name, "，分数：", score)  # 输出序号、学生姓名和分数

print("\n小案例：找出分数最高的学生")  # 输出提示文字，说明下面是一个综合小案例
top_name = ""  # 创建变量 top_name，用来保存当前分数最高的学生姓名
top_score = 0  # 创建变量 top_score，用来保存当前最高分

for name, score in student_scores.items():  # 遍历每个学生姓名和对应分数
    if score > top_score:  # 判断当前学生分数是否比已经记录的最高分更高
        top_name = name  # 如果当前分数更高，就把当前学生姓名保存为最高分学生
        top_score = score  # 如果当前分数更高，就把当前分数保存为最高分

print("最高分学生是：", top_name)  # 输出最高分学生的姓名
print("最高分是：", top_score)  # 输出最高分的具体数值

print("\n补充：使用 get() 安全读取字典中的值")  # 输出提示文字，说明下面演示 get() 方法
xiaoming_score = student_scores.get("小明")  # 使用 get() 根据键“小明”读取对应分数
unknown_score = student_scores.get("小李", "没有找到这个学生")  # 使用 get() 读取不存在的键，并设置默认提示

print("小明的分数：", xiaoming_score)  # 输出小明的分数
print("小李的分数：", unknown_score)  # 输出小李的查询结果
