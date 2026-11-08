print("=== 用 is 判断内存地址 ===")
a = 10
b = 10
print(f"a 的内存地址：{id(a)}")
print(f"b 的内存地址：{id(b)}")
print(f"a is b：{a is b}")
print(f"a == b：{a == b}")
print("\n=== 用 == 判断值 ===")
c = "hello"
d = "hello"
print(f"c 的内存地址：{id(c)}")
print(f"d 的内存地址：{id(d)}")
print(f"c is d：{c is d}")
print(f"c == d：{c == d}")
print("\n=== 用 is 判断内存地址 ===")
e = 10
f = 10
print(f"e 的内存地址：{id(e)}")
print(f"f 的内存地址：{id(f)}")
print(f"e is f：{e is f}")
print(f"e == f：{e == f}")
print("\n=== 用 is 判断内存地址 ===")
g = 10
h = 10
print(f"g 的内存地址：{id(g)}")
print(f"h 的内存地址：{id(h)}")
print(f"g is h：{g is h}")
print(f"g == h：{g == h}")

age = 20
has_id = True

print(age >= 18 and has_id)#and   并且

is_vip = False
has_coupon = True

print(is_vip or has_coupon)#or    或者

is_raining = False

print(not is_raining)#not   取反