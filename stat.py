import pandas as pd
import numpy as np

#read file
df1 = pd.read_csv("data/test_case.csv")

#intersection_id count 
intersection_id = df1["intersection_id"]
unique_intersection_id = intersection_id.unique()
print "unique_intersection_id.count = ",
print len(unique_intersection_id)

#tollgate_id count 
tollgate_id = df1["tollgate_id"]
unique_tollgate_id = tollgate_id.unique()
print "unique_tollgate_id.count = ",
print len(unique_tollgate_id)

#vehicle_id count 
vehicle_id = df1["vehicle_id"]
unique_vehicle_id = vehicle_id.unique()
print "unique_vehicle_id.count = ",
print len(unique_vehicle_id)

# road_id#start_time#time_spent
# 105#2016-07-19 00:14:24#9.56;
# 100#2016-07-19 00:14:34#6.75;
# 111#2016-07-19 00:14:41#13.00;
# 103#2016-07-19 00:14:54#7.47;
# 122#2016-07-19 00:15:02#32.85

travel_seq = df1["travel_seq"]
print travel_seq.head()
