import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math':[32, 55, 67, 55, 100]}
data1 = {'ch': ['gz', 'sx', 'bj', 'sh']}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZF', 'GY', 'ZY', 'HZ', 'LB'])
df3 = DataFrame(data1)
print df1
print df2
# df2['Chinese'].astype(np.int64)
# df2['Chinese'].astype('str')
# df2['English'].map(str.strip)
df2.columns = df2.columns.str.upper()
print df2
