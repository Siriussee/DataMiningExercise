import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


# read file
df1 = pd.read_csv("data/test_case.csv")

# road_id#start_time#time_spent
# 105#2016-07-19 00:14:24#9.56;

travel_seq = df1["travel_seq"]
single_travel_seq = []

for each_travel_seq in travel_seq:
    temp = each_travel_seq.split(';')
    for each in temp:
        single_travel_seq.append(each)

# get hour data in ROAD 120 & DATE 2016-07-23
target_data = np.zeros(shape=(600,2))
# [hour, time_spent]
i = 0
for each in single_travel_seq:
    if each.split('#')[0] == '120' and each.split('#')[1].split(' ')[0] == '2016-07-23':
        target_data[i] = [int(each.split('#')[1].split(' ')[1].split(':')[0]),float(each.split('#')[2])]
        i = i+1
# print target_data

mean_time_spent = []
for x in range(24):
    sum = 0
    count = 0
    for each in target_data:
        if x == each[0]:
            print each[1]
            sum += each[1]
            count = count+1
    if count == 0:
        mean_time_spent.append(0)
    else:        
        mean_time_spent.append(sum/count)

# print mean_time_spent

series_mean_time_spent = pd.Series(mean_time_spent)

print series_mean_time_spent

plt.plot(series_mean_time_spent.index, series_mean_time_spent)

plt.show()
            


