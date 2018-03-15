import pandas as pd
import numpy as np

# read file
df1 = pd.read_csv("data/test_case.csv")

# road_id#start_time#time_spent
# 105#2016-07-19 00:14:24#9.56;
# 100#2016-07-19 00:14:34#6.75;
# 111#2016-07-19 00:14:41#13.00;
# 103#2016-07-19 00:14:54#7.47;
# 122#2016-07-19 00:15:02#32.85

travel_seq = df1["travel_seq"]
print travel_seq.head(1)

# test str.split('mark')
# print travel_seq[0].split(';')[0].split('#')[0]

road_id_arr = np.array([])
np.insert(road_id_arr,0,travel_seq[0].split(';')[0].split('#')[0])

print road_id_arr