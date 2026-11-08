s3 = """一行文字
二行文字
三行文字
四行文字"""
print(s3)

quote1 = 'hi:"heloo"'
quote2 = "hi:'world'"
print(quote1)
print(quote2)

print("\n=== 常见转义字符 ===")

print("\\: 反斜杠")
print("\\n: 换行")
print("\\t: 制表符")
print("\\r: 回车")
print("\\b: 退格")
print("\\f: 换页")
print("\\a: 响铃")
print("\\v: 垂直制表符")
print("\\ooo: 八进制数")
print("\\xhh: 十六进制数")
print("\\uhhhh: 十六进制数")
print("\\Uhhhhhhhh: 十六进制数")

print("\n=== 字符串索引 ===")
s = "hello"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print("hello的长度是：", len(s))

print("\n=== 字符串切片 ===")
s = "hello"
print(s[0:3])
print(s[1:4])
print(s[2:5])
print(s[3:6])
print(s[4:7])

print("\n=== 字符串拼接 ===")
s1 = "hello"
s2 = "world"
print(s1 + s2)
print(s1 * 3)
print(s1[0:3] + s2[0:3])
print(s1[0:3] * 3)
print(s1[0:3] + s2[0:3] * 3)
print(s1[0:3] + s2[0:3] * 3)

print("\n=== 字符串格式化 ===")
name = "张三"
age = 20
print("我的名字是：%s，我的年龄是：%d" % (name, age))
print("我的名字是：{0}，我的年龄是：{1}".format(name, age))
print("我的名字是：{name}，我的年龄是：{age}".format(name=name, age=age))
print("我的名字是：{name}，我的年龄是：{age}".format_map(locals()))
print("我的名字是：{name}，我的年龄是：{age}".format_map(globals()))
print("我的名字是：{name}，我的年龄是：{age}".format_map(locals()))

print("\n=== 大小写字符串方法 ===")
s = "hello"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.casefold())
print(s.center(10))
print(s.ljust(10))
print(s.rjust(10))
print(s.zfill(10))

