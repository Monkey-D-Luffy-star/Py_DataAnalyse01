from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ['战狼2','哪吒之魔童降世','流浪地球','红海行动','美人鱼','唐人街探案2','我和我的祖国','我不是药神','中国机长','速度与激情8']
b = [56.39,49.34,46.18,36.22,33.9,33.71,31.46,30.75,28.84,26.49]
x = range(len(a))

myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

plt.figure(figsize=(10,6),dpi=80)

plt.bar(x,b,width=0.3)

plt.xticks(x,a,fontproperties=myfont,size=16,rotation=45)

plt.show()