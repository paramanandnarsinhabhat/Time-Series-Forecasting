import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


from sklearn.metrics import mean_squared_error
from math import sqrt

import warnings
warnings.filterwarnings("ignore")

train_data = pd.read_csv("/Users/paramanandbhat/Downloads/4.1_naive_approach/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/4.1_naive_approach/data/valid_data.csv")


print(train_data.shape)
train_data.head()

print(train_data.head())

train_data.tail()

print(train_data.tail())

#Required Preprocessing
train_data.timestamp = pd.to_datetime(train_data['Date'],format='%Y-%m-%d')
train_data.index = train_data.timestamp


valid_data.timestamp = pd.to_datetime(valid_data['Date'],format='%Y-%m-%d')
valid_data.index = valid_data.timestamp

plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.legend(loc='best')
plt.title("Train and Validation Data")
plt.show()

print(train_data.Date.min(), train_data.Date.max())

#Naive Model
print(train_data.shape)
print(train_data.tail())

# indexing starts from 0
train_data['count'][577]

# Defining predictions for validation
valid_data['naive'] = train_data['count'][577]

plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.plot(valid_data.index,valid_data['naive'], label='Naive Forecast')
plt.legend(loc='best')
plt.title("Naive Approach")
plt.show()

# calculating RMSE 
rmse = sqrt(mean_squared_error(valid_data['count'], valid_data['naive']))
print('The RMSE value for Naive Approach is', rmse)