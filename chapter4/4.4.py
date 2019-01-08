# test 1
#列表切片
names = ["Amy","Sam","Ziv","Leo","Rock"]
# 输出索引为1~3的元素，同样的，不包含3
print(names[1:3])
# 不指定起始索引，默认从开头开始
print(names[:3])
# 不指定结尾索引，默认到列表的结尾
print(names[2:])
# 用负数输出倒数几个元素
print(names[-2:])


# test 2
#与完整的列表相同，切片也是可以被遍历的
for name in names[:3]:
    print(name)


# test 3
# 列表的复制,使用一个包含所有元素的切片
name3 = names[:]
names.append("ming")
name3.append("wa")
print(names)
print(name3)

name4 = names
name4.append("1")
names.append("2")
print(name4)
print(names)
'''
值得注意的是，使用切片复制的列表才是真正的创建了一个新的独立的列表，两者之间的修改互不干扰
而使用赋值的方式赋值的列表只是将两个变量都指向了同一个列表，在两者上的操作会反映在同一个列表上
'''