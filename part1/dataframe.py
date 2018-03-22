'''
- Two-dimensional size-mutable array with labeled axes
- +-*/ different labeled matrix, will combine;
- only when same lable & col & row can work
- pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
                matrix value  row name    column name
- view dataframs
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
print dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

df02 = pd.DataFrame(np.random.randint(low=0, high=10, size=(4, 4)),columns=['a', 'b', 'c', 'd'])
print df02

print df+df02

df3 = pd.DataFrame(np.random.randint(low=0, high=10, size=(6, 4)),index=dates,columns=['A', 'B', 'C', 'D'])

print df+df3

df2 = pd.DataFrame({          'A' : 1.,
                      'B' : pd.Timestamp('20130102'),
                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                      'D' : np.array([3] * 4,dtype='int32'),
                      'E' : pd.Categorical(["test","train","test","train"]),
                      'F' : 'foo' })

print "df.head(2) = "
print df.head(2)

print "df.tail(3) = "
print df.tail(3)