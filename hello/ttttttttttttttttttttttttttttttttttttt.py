import pandas

a = [1, 1, 1, 0, 0, 0]
b = [[1, 2],
     [3, 4],
     [5, 6],
     [7, 8]]
import numpy as np
c=np.array(a)
d=np.array(b)
# sasa = d[c == 0, 0]
print(c==1)
print(pandas.DataFrame(b))