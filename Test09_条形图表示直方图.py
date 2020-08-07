from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

# 绘制画布
plt.figure(figsize=(15,8),dpi=80)

# 绘制条形图
x = range(len(interval))
plt.bar(x,quantity,width=1)             # 实际的x坐标

# 设置x坐标
_x = [i-0.5 for i in range(len(interval)+1)]
_x_ticks = interval+[150]
plt.xticks(_x,_x_ticks)          #实际显示的x坐标

# 设置网格
plt.grid(alpha=0.3)

# 显示图像
plt.show()
