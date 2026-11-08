# Python 列表学习案例：增删改查、切片、排序、浅拷贝、深拷贝

import copy  # 导入 copy 模块，用来使用 deepcopy() 做深拷贝

print("========== 1. 创建列表 ==========")  # 打印标题，方便区分输出内容
scores = [88, 76, 92, 65, 99]  # 创建一个列表，用来保存多个学生的成绩
print("初始成绩：", scores)  # 打印当前列表，查看一开始有哪些成绩

print("========== 2. 列表增加 ==========")  # 打印标题，说明下面演示列表添加数据
scores.append(80)  # 增：在列表最后添加一个成绩 80
print("append 添加后：", scores)  # 打印列表，查看 append 添加后的结果
scores.insert(1, 70)  # 增：在索引 1 的位置插入成绩 70，原来的元素会往后移动
print("insert 插入后：", scores)  # 打印列表，查看 insert 插入后的结果
scores.extend([60, 85])  # 增：一次性把另一个列表里的多个成绩添加到末尾
print("extend 批量添加后：", scores)  # 打印列表，查看 extend 批量添加后的结果

print("========== 3. 列表查询 ==========")  # 打印标题，说明下面演示查询列表数据
first_score = scores[0]  # 查：通过索引 0 获取列表中的第一个成绩
print("第一个成绩：", first_score)  # 打印第一个成绩
last_score = scores[-1]  # 查：通过索引 -1 获取列表中的最后一个成绩
print("最后一个成绩：", last_score)  # 打印最后一个成绩
has_92 = 92 in scores  # 查：判断列表中是否存在 92 这个成绩
print("列表里是否有 92 分：", has_92)  # 打印判断结果，True 表示有，False 表示没有
score_count = len(scores)  # 查：使用 len() 获取列表中一共有多少个元素
print("成绩数量：", score_count)  # 打印成绩的数量
index_92 = scores.index(92)  # 查：获取成绩 92 在列表中的索引位置
print("92 分的位置索引：", index_92)  # 打印 92 这个成绩所在的位置

print("========== 4. 列表修改 ==========")  # 打印标题，说明下面演示修改列表数据
scores[2] = 95  # 改：把索引 2 位置上的成绩修改成 95
print("修改索引 2 后：", scores)  # 打印列表，查看修改后的结果

print("========== 5. 列表删除 ==========")  # 打印标题，说明下面演示删除列表数据
removed_score = scores.pop()  # 删：删除列表最后一个元素，并把被删除的值保存下来
print("pop 删除的成绩：", removed_score)  # 打印刚才被 pop 删除的成绩
print("pop 删除后：", scores)  # 打印列表，查看 pop 删除后的结果
scores.remove(65)  # 删：删除列表中第一个值为 65 的元素
print("remove 删除 65 后：", scores)  # 打印列表，查看 remove 删除后的结果
del scores[0]  # 删：删除索引 0 位置上的元素
print("del 删除索引 0 后：", scores)  # 打印列表，查看 del 删除后的结果

print("========== 6. 列表切片 ==========")  # 打印标题，说明下面演示列表切片
first_three = scores[0:3]  # 切片：取索引 0 到索引 2 的元素，不包含索引 3
print("前三个成绩：", first_three)  # 打印切片得到的前三个成绩
last_two = scores[-2:]  # 切片：从倒数第 2 个元素开始，一直取到最后
print("最后两个成绩：", last_two)  # 打印最后两个成绩
middle_scores = scores[1:4]  # 切片：取索引 1 到索引 3 的元素，不包含索引 4
print("中间一段成绩：", middle_scores)  # 打印中间这一段成绩
reverse_scores = scores[::-1]  # 切片：从后往前取，相当于把列表倒过来
print("倒序查看成绩：", reverse_scores)  # 打印倒序后的列表

print("========== 7. 列表排序 ==========")  # 打印标题，说明下面演示列表排序
scores.sort()  # 排序：直接修改原列表，让成绩从小到大排列
print("升序排序后：", scores)  # 打印从小到大排序后的列表
scores.sort(reverse=True)  # 排序：直接修改原列表，让成绩从大到小排列
print("降序排序后：", scores)  # 打印从大到小排序后的列表
new_scores = sorted(scores)  # 排序：生成一个新的升序列表，原列表不会被改掉
print("新的升序列表：", new_scores)  # 打印 sorted() 生成的新列表
print("原来的列表：", scores)  # 打印原列表，观察 sorted() 不会改变原列表

print("========== 8. 浅拷贝 ==========")  # 打印标题，说明下面演示浅拷贝
students = [["小明", [80, 90]], ["小红", [88, 92]]]  # 创建一个嵌套列表，每个学生里面又有一个成绩列表
shallow_students = students.copy()  # 浅拷贝：复制最外层列表，但里面的小列表还是共用的
print("原列表 students：", students)  # 打印原列表，查看原始数据
print("浅拷贝 shallow_students：", shallow_students)  # 打印浅拷贝列表，观察内容和原列表一样
print("原列表内层成绩 id：", id(students[0][1]))  # 打印原列表里第一个学生成绩小列表的身份编号
print("浅拷贝内层成绩 id：", id(shallow_students[0][1]))  # 打印浅拷贝里第一个学生成绩小列表的身份编号
students[0][1][0] = 100  # 修改原列表里小明的第一个成绩，因为内层列表共用，所以浅拷贝也会受影响
print("修改原列表内层成绩后 students：", students)  # 打印原列表，查看修改后的数据
print("修改原列表内层成绩后 shallow_students：", shallow_students)  # 打印浅拷贝列表，观察它也被影响了

print("========== 9. 深拷贝 ==========")  # 打印标题，说明下面演示深拷贝
students = [["小明", [80, 90]], ["小红", [88, 92]]]  # 重新创建一个嵌套列表，避免被上面的修改影响
deep_students = copy.deepcopy(students)  # 深拷贝：外层列表和里面的小列表都会复制一份
print("原列表 students：", students)  # 打印原列表，查看原始数据
print("深拷贝 deep_students：", deep_students)  # 打印深拷贝列表，观察内容和原列表一样
print("原列表内层成绩 id：", id(students[0][1]))  # 打印原列表里第一个学生成绩小列表的身份编号
print("深拷贝内层成绩 id：", id(deep_students[0][1]))  # 打印深拷贝里第一个学生成绩小列表的身份编号
students[0][1][0] = 100  # 修改原列表里小明的第一个成绩，因为深拷贝完全独立，所以深拷贝不会受影响
print("修改原列表内层成绩后 students：", students)  # 打印原列表，查看修改后的数据
print("修改原列表内层成绩后 deep_students：", deep_students)  # 打印深拷贝列表，观察它没有被影响

print("========== 10. 总结 ==========")  # 打印标题，说明下面输出总结
print("浅拷贝：只复制外层列表，里面嵌套的小列表还是共用。")  # 打印浅拷贝的大白话总结
print("深拷贝：外层和内层都复制一份，修改原列表不会影响深拷贝。")  # 打印深拷贝的大白话总结
