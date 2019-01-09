# test 1
cars = ["bwm","loslias","toyota","Audi"]
for car in cars:
    if car.lower() == "audi":
        print(car.upper())
    else:
        print(car.title())
'''
python中大小写不同，比较得到的结论为不等
如果想忽略大小写进行比较，可以用lower()函数将两者均变为小写（临时）再进行比较
'''


# test 2
if car[2] != "2333":
    print("yep")
else:
    print("osh")
'''
数值检测等或不等与上述方法相同
'''


# test 3
# 多个条件的判断
# and表示'且'；or表示'或'
if 2<=1 and 3>=2:
    print("2<=1 and 3>=2")
elif 2<=1 or 3>=2:
    print("2<=1 or 3>=2")
'''
注意else if 在python中要写作elif
最后的else可以省略
可以多个if语句并列使用
'''


# test 4
# 检查特定关键字是否在列表/元组中
if "bwm" not in cars:
    print("bwm is not in cars")
else:
    print("bwm is in cars")


# test 5
bool_ = True
bool__ = False
print(bool_)
print(bool__)
'''
布尔表达式，要么为True，要么为False
注意True和False的首字母必须大写
'''

# test 6
# 确定列表不空
if cars:
    print("列表不空")
else:
    print("列表为空")