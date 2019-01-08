# test 1
# range()函数
for i in range(1,5):
    # 打印1~5之间的整数不包含5
    print(i)


# test 2
# 使用range()创建数字列表
nums1 = list(range(1,6))
print(nums1)


# test 3
# 使用range()函数，指定步长
nums2 = list(range(0,11,2))
print(nums2)


# test 4
# 0~10  以内平方计算
square = []
for i in range(1,11):
    square.append(i*i)

print(square)


#对列表的简单统计
print(min(square))
print(max(square))
print(sum(square))


# 列表解析的方式创建列表
squ = [value*2 for value in range(1,11)]
print(squ)



