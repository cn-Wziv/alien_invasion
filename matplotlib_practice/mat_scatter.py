import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x**2 for x in x_values]
# 绘制散点图，设置点的颜色为(0, 0, 0.8),点的外围颜色为黑色，指定点的大小为40
# plt.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors='black', s=40)
# 使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=24)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()