age = 18
name = "小明"

age = 200

print("年龄：",age)
print("名字：",name)

a = 100
print("a的值是：",a)

a = "200"
print("a的值是：",a)

x,y,z = 1,2,3
print("x=",x , "y=",y , "z=",z)

a = b = c = 100
print("a=",a , "b=",b , "c=",c)


left = "左手拿着苹果"
right = "右手拿着香蕉"
print("交换前：",left,"|",right)

left,right = right,left
print("交换后：",left,"|",right)

#变量命名规范：变量名只能包含字母、数字和下划线。变量名不能以数字开头。变量名不能包含空格。
# 变量名不能包含特殊字符。变量名不能包含关键字。变量名不能包含空格。变量名不能包含特殊字符。
# 变量名不能包含关键字。变量名不能包含空格。变量名不能包含特殊字符。变量名不能包含关键字。
import keyword
print("python 关键字列表:")
print(keyword.kwlist)
print("python 关键字列表长度：",len(keyword.kwlist))