# test 1
'''
调用 open() 时提供了两个实参。
第一个实参也是要打开的文件的名称；第二个实参告诉Python，我们要以何种模式打开这个文件。打开文件时，
可指定读取模式 （ 'r' ）、写入模式（ 'w' ）、附加模式（ 'a' ）或让你能够读取和写入文件的模式（ 'r+' ）
'''
filename = "test1"

with open(filename, 'w') as file_object:
    file_object.write("I love programing.")
    file_object.write("\nHello world")

#  附加模式打开的文件，写入的内容会追加到文件末尾
with open(filename,'a') as file_object:
    file_object.write('\nadding something')

# test 2
# 从控制台读取内容写入文件
import time
target = 'true'
while target != 'quit':
    name = input("Please input your name:\n")
    target = name
    if target != 'quit':
        print("hello {}".format(name))

        with open('access_log','a') as file:
            file.write(name + '\n')