import numpy as np
a= np.ones((9,9),dtype=np.int16)##制造一个9*9的值为1的数组
b=a.cumsum(axis=1)##每一列累积
print(b*(b.T))##转置相乘
