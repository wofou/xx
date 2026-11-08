# 这就是集合
from typing import Any

s = {1, 2, 3, 4, 1}
print(s)
print(type(s))
# 空集合必须这么写（不能写 {}，那是空字典）
empty_set = set[Any]()

s = {1, 2, 2, 3, 3, 3}
print(s)  # 输出：{1,2,3}  重复的自动没了！

my_list = [1, 2, 2, 3, 3, 3]
my_list = list(set(my_list))  # 去重神器
print(my_list)  # [1,2,3]

s = {1, 2, 3}
print(2 in s)  # True
print(5 in s)  # False

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # 交集：{3} 共同的
print(a | b)  # 并集：{1,2,3,4,5} 合并去重
print(a - b)  # 差集：{1,2} a有b没有的