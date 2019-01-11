# test 1
# 列表间元素的移动
unfirmed_name = ['alice','amy','lili']
firmed_name = []
while unfirmed_name:
    username = unfirmed_name.pop()

    print("Verifying name :" + username.title())
    firmed_name.append(username)

print("\nThe following name is confirmed:")
while firmed_name:
    print(firmed_name.pop())


print('===========================================================================================')
# test 2
# 删除列表中的多个相同的元素
animals = ['dog','cat','pig','chicken','cat']
while 'cat' in animals:
    animals.remove('cat')
    print('Removed a cat')


# test 3
# 用输入填充字典
responses = {}
name = input("What's your name ?\n")
responses['name'] = name

age = input("what's your age ?\n")
responses['age'] = age

print(responses['name'].title() + "'s age is " + responses['age'])
