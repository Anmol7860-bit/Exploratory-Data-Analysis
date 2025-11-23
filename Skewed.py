#how to deal wirh skewed data 

#importing dependencies
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import os 

df=pd.read_csv('kc_house_data.csv')
print(df.head())