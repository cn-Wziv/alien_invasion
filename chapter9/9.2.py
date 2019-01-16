# test 1
# 继承
'''
继承时，创建子类实例时，需要先对父类的所有属性赋值
父类必须与子类位于同一文件中，且父类必须在子类之前
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("I'm a method in father class.")

# 子类class 子类名(父类名):
class ElectricCar(Car):
    # 子类初始化函数初始化父类所有属性
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    # 子类定义额外的方法
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
# 子类实例化对象调用从父类继承来的方法
print(my_tesla.get_descriptive_name())

# 子类实例化对象调用子类自己的方法
my_tesla.describe_battery()

'''
实例可以作为其他类的属性
可以在模块中存储多个类，用到的时候在其他模块中导入即可
可以从一个模块中导入其中的类，可以从一个模块中导入另一个模块中的所有类
可以导入整个模块
'''

'''
类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划线。
实例名和模块名都采用小写格式，并在单词之间加上下划线

对于每个类，都应紧跟在类定义后面包含一个文档字符串。
这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
'''