print("=== 用 type() 查看类型===")

a = 42
b = 3.14
c = True
d = "你好"
e = None

print(f"42    的类型：{type(a)}")
print(f"3.14  的类型：{type(b)}")
print(f"true  的类型：{type(c)}")
print(f"你好  的类型：{type(d)}")
print(f"None  的类型：{type(e)}")

print("\n=== 用 isinstance() 判断类型 ===")

age = 18
name = "小明"

print(f"age 是 int 嘛? {isinstance(age,int)}")
print(f"age 是 str 嘛? {isinstance(age,str)}")
print(f"name 是 str 嘛? {isinstance(name,str)}")

print("\n=== int() 转整数 ===")

print('int("123") → ' ,int("123"))
print('int(3.9) → ' ,int(3.9))
print('int(True) → ' ,int(True))
print('int(False) → ' ,int(False))

print("\n=== flota() 浮点数 ===")

print('float("3.14") → ' ,float("3.14"))
print('float("100") → ' ,float("100"))
print('float(42) → ' ,float(42))
print('float(True) → ' ,float(True))

print("\n=== str() 转字符串 ===")

print("str(123) →",repr(str(123)))
print("str(3.14) →",repr(str(3.14)))
print("str(True) →",repr(str(True)))
print("str(None) →",repr(str(None)))

print("\n=== bool() 布尔值 ===")

print("bool(1) →",bool(1))
print("bool(0) →",bool(0))
print('bool("hi") →',bool("hi"))
print("bool("") →",bool(""))
print("bool(None) →",bool(None))