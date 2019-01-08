# 4-3
for i in range(1,101):
    print(i)


# 4-4
nums = [j for j in range(1,1000001)]
print(nums)


# 4-5
# 1~10的立方解析
cube = [j**3 for j in range(1,11)]
print(cube)


# 4-6
# 1~1000000的和
import time
start = time.clock()
sum = sum(nums)
end = time.clock()
print(sum)
print("计算时间为：" + str(end - start))