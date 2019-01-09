# test 1
customs = ["lili", "amy", "sam", "fox"]
if customs:
    for custom in customs:
        if custom == "amy":
            print("hello amy, would you like to see some status report")
        else:
            print("hello " + custom + " , thanks for logging in.")
else:
    print("We need to find some users")


print("===========================================================================================")

# test 2
names = ["daming","lili","lingling","rex"]
new_names = ["Daming", "amy", "sam"]

for name in names:
    for new_name in new_names:
        if new_name.lower() == name.lower():
            print(new_name + " you need find a new name")


print("===========================================================================================")

# test 3
nums = [num for num in range(1,10)]

for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    else:
        print(str(num) +"th")



'''
在诸如 == 、 >= 和 <= 等比较运算符两边各添加一个空格，例如， if
age < 4: 要比 if age<4: 好
'''