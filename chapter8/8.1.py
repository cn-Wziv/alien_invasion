# test 1
# 函数
def greet_user1():
    print("Hello world !")

greet_user1()


print("===========================================================================================")
# test 2
# 传参:username是形参；jessi是实参
def greet_user2(username):
    print("hello {}".format(username))

greet_user2("jessi")


print("===========================================================================================")
# test 3
# 位置实参：顺序必须一致
def describe_animal(animal_type, animal_name):
    print(animal_name + " is a " + animal_type)

describe_animal("pig", "peiqi")
describe_animal("dog", "sinba")


print("===========================================================================================")
# test 4
# 关键字实参：键值对
describe_animal(animal_type="cat",animal_name="tom")


print("===========================================================================================")
# test 5
# 默认值
def describe_pet(pet_name, pet_type="dog"):
    print(pet_name + " is a " + pet_type)

describe_pet(pet_name="wangcai")


print("===========================================================================================")
# test 6
# 返回值
def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("lebron", "james").title())

# 使用默认值使参数变得可选， 只在必要是才会对默认值进行传参


print("===========================================================================================")
# test 7
'''
返回值可以是各种类型的值，包括字典， 列表， 元组， 数组等
'''


print("===========================================================================================")
# test 8
# 传参串列表
def greet_users(names):
    for name in names:
        print("hello {}".format(name).title())

names = ["amy", "baly", "cindy"]
greet_users(names)


print("===========================================================================================")
# test 9
'''
若明确要求列表不能被修改，可以通过传其副本实现
即传递其包含所有元素的切片
'''
greet_users(names[:])


print("===========================================================================================")
# test 10
'''
传递任意数量的参数
形参设置成指针形式，调用时传递的若干参数全部存储在相应的列表或字典中
可以与各种方式的传参方法结合：位置实参+任意数量的参数；
'''
def make_pizza(*toppings):  #任意参数存在列表中
    for topping in toppings:
        print(topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

def sell_book(**books):
    for name,price in books.items():
        print(name,price)

sell_book(a=12, b=13, c=14)