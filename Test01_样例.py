from matplotlib import pyplot as plt
x = range(2,26,2)
y = [14,15,18,20,25,24,23,15,19,21,16,22]
# 设置图片大小
plt.figure(figsize=(20,8),dpi=80)
# 绘图
plt.plot(x,y)
x_ticks = [i/2 for i in range(4,49)]
# 设置x坐标
plt.xticks(x_ticks[::3])
plt.yticks(range(min(y),max(y)+1))
# 保存图片
# plt.savefig('./t1.png')
# 显示图片
plt.show()
