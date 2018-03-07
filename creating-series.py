'''
Series Exercise
- use of NaN
- One-dimensional ndarray with axis labels
- +-*/

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6])

print "s = "
print s

a = pd.Series([2,4,6,8,10])
b = pd.Series([2,2,2,2,2])
c = pd.Series([1,1,1,1])
d = pd.Series([1,1,1,1,np.nan])

print "s-a = "
print s-a

print "a*b = "
print a*b

print "a/b = "
print a/b

print "a*c = "
print a*c

print "a*d = "
print a*d

