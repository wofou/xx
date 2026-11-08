print("=== 算数运算符 ===")

a = 17
b = 5
print(f"a = {a}, b = {b}")
print(f"加法   a + b = {a + b}")
print(f"减法   a - b = {a - b}")
print(f"乘法   a * b = {a * b}")
print(f"除法   a / b = {a / b}")
print(f"整除   a // b = {a // b}")
print(f"幂运算   a ** b = {a ** b}")

print("\n=== 整除和取余的实际用途 ===")

total_seconds = 9527

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds =total_seconds % 60
print(f"{total_seconds} 秒 = {hours} 小时 {minutes} 分钟 {seconds} 秒")