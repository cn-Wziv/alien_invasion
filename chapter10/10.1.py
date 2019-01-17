# test 1
'''
想要操作任何文件都要先打开
使用with关键字，可以在文件不使用时自动关闭，而不用再必须使用close()函数手动关闭
with代码快打开的文件只能在with代码块中使用，想要再代码块外使用文件内容，需要将文件存储在一个列表中
'''
with open('pi_digits') as file_object:
    content = file_object.read()
    print(content)

'''
linux和macOS中的决对路径中用‘/’隔开
windows中的绝对路径用‘\’隔开
'''

# test 2
# 逐行打印
with open('pi_digits') as file_object:
    for line in file_object:
        # 使用restrip()函数去除行尾的空格
        print(line.rstrip())


# test 3
# 在代码块之外使用文件内容
with open('pi_digits') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())