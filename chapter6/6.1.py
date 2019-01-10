# test 1
'''
字典以‘{}’标识，其中的元素是键值对
通过指定键来访问其对应的值
'''
#
alien = {'color':'green', 'age':'14', 'sex':'male'}
print(alien['color'])
print(alien['sex'])
print(alien['age'])


# test 2
# 创建空字典，添加键值对
alien_ = {}
alien_['x_pos'] = 10
alien_['y_pos'] = 20

print(alien_['x_pos'])


# test 3
# 修改键值对
alien['color'] = 'yellow'
print(alien['color'])

# 删除键值对
del alien['age']
print(alien)


# 遍历字典
# 字典的items()函数返回字典键值对的列表
for key,value in alien.items():
    print(key+":"+value)

# 字典的key()
for key in alien.keys():
    print(key)

# 字典的value()
for value in alien.values():
    print(value)

# 以特定顺序输出键
# 使用sorted()对返回的字典的键的列表进行临时排序
for key in sorted(alien.keys()):
    print(key)