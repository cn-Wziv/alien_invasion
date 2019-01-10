# test 1
# 嵌套
# 创建30个外星人字典：列表中嵌套字典
aliens = []
for alien_num in range(1,31):
    alien = {'color':'green', 'age':'14', 'point':'5', 'number':alien_num}
    aliens.append(alien)


# 修改前3个，用到切片
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['age'] = '20'
        alien['point'] = '10'

for alien in aliens:
    print(alien)



# 披萨店的点餐：字典中嵌套列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese']
}
# 仅访问其中的列表
for topping in pizza['toppings']:
    print(topping)


# 网站用户登记：字典中嵌套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())