# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 02:08:22 2021

@author: conor
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 07:22:29 2021

@author: conor
"""
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2

from sklearn.datasets import load_digits

import pandas as pd
from emmv import emmv_scores
import sys
print('#Hello from python#')
print('First param:'+sys.argv[1]+'#')
print('Second param:'+sys.argv[2]+'#')

# #Read in dataset
# #First 100 rows
# testset = pd.read_csv('human_activity_raw_sensor_data/sensor_sample_float.csv', nrows=7000,parse_dates=['timestamp'])

# # print(testset.dtypes)

# #change timestamp to an int so clf will work
# testset['timestamp'] = pd.to_numeric(testset['timestamp'])

# #split the data into training and test sets
# train, test = train_test_split(testset, test_size=0.3)

# #sort the train set by its timestamp
# train = train.sort_values(['timestamp'])

# #use the value and timestamp columns 
# clf = IsolationForest().fit(train[['value','timestamp','sensor_id']])

# #use the model to predict the values in the testset
# results = clf.predict(test[['value','timestamp','sensor_id']])

# test_scores = emmv_scores(clf,test[['value','timestamp','sensor_id']])

# print(test_scores)

# # create date time features of a dataset
# series = pd.read_csv('human_activity_raw_sensor_data/sensor_sample_float.csv',parse_dates=['timestamp'], squeeze=True, nrows=7000)

# print(series.dtypes)

# print(series.shape)

# print(X_new = SelectKBest(chi2, k=20).fit_transform(series))

# dataframe = pd.DataFrame()
# dataframe['timestamp'] = [series.index[i] for i in range(len(series))]
# dataframe['value'] = [series.index[i] for i in range(len(series))]
# dataframe['sensor_id'] = [series.index[i] for i in range(len(series))]
# print(dataframe.head(5))
