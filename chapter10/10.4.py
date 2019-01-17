# test 1
# 使用json存储运行过程中产生的数据
# 使用json.dump(date,file)存储数据
import json

num = ['1','2','3','4']
with open("num.json", 'w') as file:
    json.dump(num, file)

# 使用json.load(file)加载json中的数据
with open('num.json') as file:
    number = json.load(file)
    print(number)