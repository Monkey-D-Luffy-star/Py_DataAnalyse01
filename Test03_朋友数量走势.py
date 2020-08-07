from matplotlib import pyplot as plt
from matplotlib import font_manager

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
x = range(11, 31)
z = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 创建字体
myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

# 设置画布大小
plt.figure(figsize=(20, 8), dpi=80)

# 画图
plt.plot(x, y,label='自己',color='#DA70D6',linestyle=':')
plt.plot(x,z,label='同桌',color='#6495ED',linestyle='--')

# 设置x轴显示
_x = ['{}岁'.format(i) for i in x]
plt.xticks(x, _x, fontproperties=myfont)
plt.yticks(range(min(y), max(y) + 1))

# 设置x,y,图的标记信息
plt.xlabel('年龄', fontproperties=myfont, size=16)
plt.ylabel('女朋友数量', fontproperties=myfont, size=16)
plt.title('从11岁到30岁每年女朋友数量变化', fontproperties=myfont, size=16)

# 绘制网格
plt.grid(alpha=0.3)  # alpha设置网格透明度

plt.legend(prop=myfont,loc='upper left')

plt.show()
