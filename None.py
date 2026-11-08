print("\n==== None 值 ====")
phone = None
print("手机号：",phone)
print("手机号类型：",type(phone))

print("\n=== 判断 None 的正确姿势 ===")
if phone is None:
    print("还没有结果")

result =100

if result is not None:
    print(f"查到了结果: {result}")
