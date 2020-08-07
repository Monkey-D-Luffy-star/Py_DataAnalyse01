from matplotlib import pyplot as plt
from matplotlib import font_manager

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]
# 设置中文字体
myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

# 设置画布的大小
plt.figure(figsize=(20, 8), dpi=80)

x_3 = range(1, 32)
x_10 = range(41, 72)        # 数字跟两幅图的间距有关，为什么？
                            # 答：因为scatter画图的时候使用了该值

# plt.figure()
plt.scatter(x_3, y_3,color='red',label='3月份')
plt.scatter(x_10, y_10,color='yellow',label='10月份')

# 画坐标轴
_x = ['3月{}号'.format(i) for i in x_3]
_x += ['10月{}号'.format(i) for i in x_3]
plt.xticks(list(x_3)+list(x_10),_x,fontproperties=myfont,size=12,rotation=45)

# 显示图像标记信息
plt.legend(loc='best',prop=myfont)
plt.title('3月和10月温度信息对比',fontproperties=myfont,size=16)
plt.xlabel('日期',fontproperties=myfont,size=16)
plt.ylabel('温度（℃）',fontproperties=myfont,size=16)

# 显示图像
plt.show()
