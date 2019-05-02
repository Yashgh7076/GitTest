# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:54:44 2018

@author: Yadnyesh
"""

import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

df_1 = pd.read_csv('F:/ZS/data/train.csv')

df_2 = pd.read_csv('F:/ZS/data/artists.csv')

df_3 = pd.read_csv('F:/ZS/data/test.csv')

# Count number of unique Artist_IDs in each of the three datasets
count_1 = df_1.artist_id.nunique()
count_2 = df_2.artist_id.nunique()
count_3 = df_3.artist_id.nunique()

#Check if Artist_IDs are the same in train and test sets

# Merge dataframes on common Artist_IDs in train and test frames
#df_check = pd.merge(df_3, df_1, on="artist_id", how="outer")
#count_4 = df_check.artist_id.nunique() # Check if the number of unique ID's is same

series_1 = df_1['artist_id']
series_2 = df_3['artist_id']
print(collections.Counter(series_1) == collections.Counter(series_2))


# Merge Train and Test Datasets with artist information from df_2
df_train = pd.merge(df_1, df_2, on="artist_id", how="left")
df_test = pd.merge(df_3, df_2, on="artist_id", how="left") 

# Check for NaN's in train and test features
print(df_train['artist_familiarity'].isnull().values.any()) 
print(df_train['artist_hotttnesss'].isnull().values.any())  

print(df_test['artist_familiarity'].isnull().values.any()) 
print(df_test['artist_hotttnesss'].isnull().values.any())       