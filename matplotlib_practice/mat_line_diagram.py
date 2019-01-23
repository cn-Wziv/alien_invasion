import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 传入squares列表，指定线条粗细为5
plt.plot(input_value, squares, linewidth=5)

# 设置标题,指定字体为24号
plt.title("Squares Numbers", fontsize=24)

# 设置x轴和y轴的标题
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 打开matplotlib显示器
plt.show()