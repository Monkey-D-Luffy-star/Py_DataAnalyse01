from matplotlib import pyplot as plt
from matplotlib import font_manager

# 字体
myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

a = ['猩球崛起:终极之战', '敦刻尔克', '蜘蛛侠:英雄归来', '战狼2']

b_14 = [2358, 399, 2358, 362]
b_15 = [12357, 156, 2045, 168]
b_16 = [15746, 312, 4497, 319]

# 绘制图像大小
plt.figure(figsize=(20, 8), dpi=80)

barWidth = 0.2
# 画图
x_14 = range(len(a))
x_15 = [i+barWidth for i in x_14]
x_16 = [i+barWidth*2 for i in x_14]
plt.bar(x_14, b_14,width=barWidth,color='red',label='14日票房')
plt.bar(x_15, b_15,width=barWidth,color='yellow',label='15日票房')
plt.bar(x_16, b_16,width=barWidth,color='blue',label='16日票房')

# 横坐标信息
plt.xticks(x_15, a, fontproperties=myfont,size=16)

# 绘制网格
plt.grid(alpha=0.3)

# 绘制标注
plt.legend(loc='upper right',prop=myfont)

# 显示图片
plt.show()
