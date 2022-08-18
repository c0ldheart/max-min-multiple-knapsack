from operator import le
import re
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
# read second list from result.txt
with open('result.txt', 'r') as f:
    result = f.readlines()
result = result[0]
result = result.strip()
# remove '[' and ']'
result = result[1:-1]
result = result.split(', ')
result = [int(i) for i in result]
result = np.array(result)
x = np.array([i for i in range(1, len(result)+1)])
# get index of maximum number in result list
max_index = np.argmax(result)
cubic_interploation_model=interp1d(x,result,kind="cubic")
# xs = range(1,4001,int(max_index/3))
# xs = [1,500,1000,max_index,2000,3000,4000]
xs = np.linspace(1, 4000,4000)
ys = cubic_interploation_model(xs)
fig, ax = plt.subplots()
# set x and y axis's label
ax.set_xlabel('number of iterations')
ax.set_ylabel('Max-Min profit')
ax.plot(xs, ys, '-')
print(result[max_index])
ax.annotate('maximum='+str(651), xy=(max_index,result[max_index]),xytext=(max_index-1500,result[max_index]-1),arrowprops=dict(arrowstyle="->",connectionstyle="angle3,angleA=0,angleB=-90"))

plt.savefig('./result1.png')
plt.show()