'''
列表是动态的，是可以改变的
元组是不可变的，不可变的列表就是元组
列表(list)使用方括号'[]'来标识
元组(tuple)使用圆括号'()'来标识
'''

# test 1
# 定义元组
square = (100,200)
print(square)

# 元组的遍历
for s in square:
    print(s)

# 试图单独修改元组元素的值是非法的
# 但可以为元组整体赋值

square = (300,400)
print(square)