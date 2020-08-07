from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ['战狼2', '哪吒之魔童降世', '流浪地球', '红海行动', '美人鱼', '唐人街探案2', '我和我的祖国', '我不是药神', '中国机长', '速度与激情8']
b = [56.39, 49.34, 46.18, 36.22, 33.9, 33.71, 31.46, 30.75, 28.84, 26.49]

# 创建字体
myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

# 绘制图像大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图像
x = range(len(a))
plt.barh(x,b,height=0.3,color='#4DFF8F')

# 设置纵坐标
plt.yticks(x,a,fontproperties=myfont,size=16)

# 设置网格线
plt.grid(alpha=0.3)

# 显示图片
plt.show()
