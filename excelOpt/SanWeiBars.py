import matplotlib.pyplot as plt

import numpy as np

X = np.arange(10)

Y = (1-X/float(10))*np.random.uniform(0.5,1.0,10) #从均匀分布中随机采样(上界、下界、样本输出数目)

plt.bar(X,Y,facecolor='pink',edgecolor='white')

for x,y in zip(X,Y):
    plt.text(x+0.05,y+0.02,'%.2f' % y,ha='center',va='bottom')

plt.xlim(-.5,10)

plt.ylim(0,1.0)

plt.xticks(())

plt.yticks(())

plt.show()