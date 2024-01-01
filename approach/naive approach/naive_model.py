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