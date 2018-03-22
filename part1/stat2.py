import pandas as pd
import numpy as np

def status(x) : 
    return pd.Series([x.count(),x.min(),x.quantile(.25),x.median(),
                      x.quantile(.75),x.mean(),x.max(),x.mad(),x.var(),
                      x.std()],index=['总数','最小值','25%分位数',
                    '中位数','75%分位数','均值','最大值','平均绝对偏差','方差','标准差'])

def get_status_according_to_road_id(road_id_x):
    travel_time_when_road_id_is_x = []
    for each in single_travel_seq:
        id = each.split('#')[0]
        if id == road_id_x:
            travel_time_when_road_id_is_x.append(each.split('#')[2])

    travel_time_when_road_id_is_x = map(eval,travel_time_when_road_id_is_x)
    print 'test:'
    # print travel_time_when_road_id_is_x
    series_travel_time_when_road_id_is_x = pd.Series(travel_time_when_road_id_is_x)
    print 'statistic of road',
    print road_id_x
    print status(series_travel_time_when_road_id_is_x)

def get_status_according_to_date(date_x):
    travel_time_when_date_is_x = []
    for each in single_travel_seq:
        date = each.split('#')[1].split(' ')[0]
        if date == date_x:
            travel_time_when_date_is_x.append(each.split('#')[2])

    travel_time_when_date_is_x = map(eval,travel_time_when_date_is_x)
    print 'test:'
    # print travel_time_when_date_is_x
    series_travel_time_when_date_is_x = pd.Series(travel_time_when_date_is_x)
    print 'statistic of date',
    print date_x
    print status(series_travel_time_when_date_is_x)
    

# read file
df1 = pd.read_csv("data/test_case.csv")

# road_id#start_time#time_spent
# 105#2016-07-19 00:14:24#9.56;
# 100#2016-07-19 00:14:34#6.75;
# 111#2016-07-19 00:14:41#13.00;
# 103#2016-07-19 00:14:54#7.47;
# 122#2016-07-19 00:15:02#32.85

travel_seq = df1["travel_seq"]
# print travel_seq.head(1)

# test str.split('mark')
# print travel_seq[0].split(';')[0].split('#')[0]

single_travel_seq = []
road_id = []
date_id = []

for each_travel_seq in travel_seq:
    temp = each_travel_seq.split(';')
    for each in temp:
        single_travel_seq.append(each)
        road_id.append(each.split('#')[0])
        date_id.append(each.split('#')[1].split(' ')[0])

unique_road_id = np.unique(road_id)
# print unique_road_id
print 'unique road id count = ',
print len(unique_road_id)

for each in unique_road_id:
    get_status_according_to_road_id(each)

unique_date_id = np.unique(date_id)
# print unique_date_id
print 'unique date count = ',
print len(unique_date_id)

for each in unique_date_id:
    get_status_according_to_date(each)