# test 1
# 用sort()进行永久性排序
car = ["bwm","audi","toyota","subaru"]
print("排序前：" + str(car))
# 默认按字母顺序排列
car.sort()
print("顺序排序后：" + str(car))
car.sort(reverse=True)
print("逆序排序后：" + str(car))


# test 2
# 使用sorted()进行临时性排序
print("临时排序：" + str(sorted(car)))
print("原列表：" + str(car))


# test 3
#翻转输出列表元素
car.reverse()
print("列表翻转后：" + str(car))

# test 4
print("列表长度为：" + str(len(car)))


'''
访问最后一个元素时尽量使用-1为索引，避免索引越界
'''