# test 1
# 导入自己编写的文件

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# test 2
# 导入特定函数
from pizza import make_pizza

make_pizza(17,'hello')


# test 3
# 导入函数并设置别名
import pizza as p
p.make_pizza(18,"as")


# test 4
# 导入模块中所有函数
from pizza import *


'''
应给函数指定描述性名称，且只在其中使用小写字母和下划线
每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式
给形参指定默认值时，等号两边不要有空格
所有的 import 语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序
'''