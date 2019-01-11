# test 1
# 循环中使用break跳出循环
mess = ""
while True:
    mess = input()
    if mess == "quit":
        break
    else:
        print(mess)

# test 2
# 循环中使用continue直接跳到下一次循环
num = 0
while num < 10:
    num = num + 1
    # 跳过偶数
    if num % 2 == 0:
        continue
    print(num)