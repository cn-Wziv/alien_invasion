'''
Python 使用被称为 异常 的特殊对象来管理程序执行期间发生的错误。
每当发生让 Python 不知所措的错误时，它都会创建一个异常对象。
如果你编写了处理该异常的代码，程序将继续运行；
如果你未对异常进行处理，程序将停止，并显示一个 traceback ，其中包含有关异常的报告。
'''

# test 1
'''
    处理异常：try-except结构
    try用于捕获异常，except用于处理异常，else中包含try中代码成功执行的后续代码
'''
try:
    print(5/0)
except ZeroDivisionError:
    pass    #什么都不做
    #print("you can't divide by zero.")
else:
    print("continue running !")