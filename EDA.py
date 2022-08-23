# look at class balance
# look at multicolinearity (wont matter if xgboost)
# descide which type of models you want to try on this
# look ad what feature engineering is needed including one hot
# identify if normalizing/standardizing is neeeded
# identify whether there are too many features and we will have to only use the most important : if so which ones
# look fofr any large out;ioers/anomolies
# check for nans (may not matter with xgboost)

### NOTES ###
# kaggle info page https://www.kaggle.com/competitions/forest-cover-type-prediction/data?select=train.csv
# most of these columns are binary (bool with 1 or 0)
# target is already in int form. need to bring in key from kaggle

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '../data/'
file = 'train.csv'

df = pd.read_csv(path + file)

print(f'shape of training data : {df.shape}')

cont_vars = ['Elevation', 'Aspect', etc]


