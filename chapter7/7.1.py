# test 1
# 输入的获取
# message = input("Please input some sent\n")
# message = int(message)  #强制类型转换
# print(message+1)
'''
input()返回的输入的都被视作字符串，应该用相应的类型转换函数强制转换
'''


# test 2
# while循环
num = 0
sum = 0
while num < 5:
    sum = sum + num
    num = num + 1

print(sum)


# test 3
# 用户选择何时退出
print("===========================================================================================")
mess = ""
while mess != "quit":
    mess = input("Please input something1:\n")
    if mess != "quit":
        print(mess)


# test 4
# 使用标志
print("===========================================================================================")
active = True
while active:
    mess = input("Please input something2:\n")
    if mess == "quit":
        active = False
    else:
        print(mess)



