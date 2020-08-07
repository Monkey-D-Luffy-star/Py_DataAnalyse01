from matplotlib import pyplot as plt
import random
import matplotlib

from matplotlib import font_manager

# 设置字体
# font = {'family' : 'Microsoft YaHei UI',
#           'weight' : 'bold',
#           'size'   : 'larger'}
# matplotlib.rc('font',**font)

# 第二种设置字体的方式
myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

# 绘制图像
plt.plot(x, y)
_x = ['10点{}分'.format(i) for i in range(60)]
_x += ['11点{}分'.format(i) for i in range(60)]

# 设置x轴显示的数据
plt.xticks(list(x)[::5], _x[::5], rotation=45,fontproperties = myfont)

# 设置提示信息
plt.xlabel('时间',fontproperties = myfont,size = 16)
plt.ylabel('温度（℃）',fontproperties = myfont,size = 16)
plt.title('10点--12点每分钟温度变化图',fontproperties = myfont,size = 16)

plt.show()
