import pandas as pd
import numpy as np

df1 = pd.read_csv("data/test_case.csv")
#print df1.head(3)

intersection_id = df1["intersection_id"]
#print intersection_id.head(3) 

unique_intersection_id = intersection_id.unique()
#print unique_intersection_id

print "unique_intersection_id.count = ",
print len(unique_intersection_id)

tollgate_id = df1["tollgate_id"]

unique_tollgate_id = tollgate_id.unique()

print "unique_tollgate_id.count = ",
print len(unique_tollgate_id)


vehicle_id = df1["vehicle_id"]

unique_vehicle_id = vehicle_id.unique()

print "unique_vehicle_id.count = ",
print len(unique_vehicle_id)


