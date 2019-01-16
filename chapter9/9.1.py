# test 1
# dog类
class Dog:
    # __init__()方法必须有，每次实例化类的时候都会执行该方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 为属性设置默认值
        self.color = 'yellow'

    def sit(self):
        print(self.name.title() + " now is sitting.")

    def roll_over(self):
        print(self.name.title() + " roll over.")

    def message(self):
        print(self.name + " is " + str(self.age) + " years old and it's color is " + self.color)

    def update_color(self, color):
        self.color = color
# 实例化
my_dog = Dog('willim', 6)

# 访问属性
print(my_dog.name + " is " + str(my_dog.age))

# 调用方法
my_dog.sit()
my_dog.roll_over()
my_dog.message()


# test 2
# 修改属性：直接访问属性并修改；通过内置方法修改
my_dog.color = 'blue'
my_dog.message()

my_dog.update_color('black')
my_dog.message()

