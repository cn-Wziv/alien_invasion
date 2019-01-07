# test 1
message1 = 'this Is "hello"'
print(message1)

# test 2
# title()将message的每一个单词的首字母大写
print(message1.title())
# upper()将字符串全部转化为大写
print(message1.upper())
# lower()将字符串全部转化为小写
print(message1.upper().lower())

# test 3
# 字符串的拼接
message2 = " world"
print(message1+" "+"\n"+message2)
# \n换行符，\t制表符

# test 4
# lstrip()删除字符串开头多余的空格，rstrip()删除字符串末尾多余的空格；strip()删除字符串两头的空格
print(message2.lstrip())
