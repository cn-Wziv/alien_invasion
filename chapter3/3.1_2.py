# test 1
# 定义列表
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles)


# test 2
# 访问列表,索引从0开始
print("第一个元素是: "+bicycles[0])

print("倒数第一个元素是："+bicycles[-1])
# 循环输出
for item in bicycles:
    print(item.title())


# test 3
# 修改列表的值
print("列表修改前：" + str(bicycles))
bicycles[2] = "bike"
print("列表修改后：" + str(bicycles))


# test 4
# 在列表末尾追加元素
bicycles.append("boat")
print("添加元素后：" + str(bicycles))

# 在列表中添加元素
'''
插入元素时，若指定的位置已经有元素，则原元素及其后续会依次后移；
若指定的位置不是原来的范围内，都会插入到原有索引范围的下一位
'''
bicycles.insert(5,"plane")
bicycles.insert(7,"flyboat")
print("插入元素后：" + str(bicycles))


# test 5
# 删除元素
del bicycles[2]
print("删除第三个元素后："+str(bicycles))

# 用pop()弹出（删除）元素并使用，默认弹出最后一个元素
print("弹出元素：" + bicycles.pop())
print("弹出第三个元素：" + bicycles.pop(2))
print("弹出元素后：" + str(bicycles))

# 用remove()删除指定的值
bicycles.remove('plane')
print(bicycles)
