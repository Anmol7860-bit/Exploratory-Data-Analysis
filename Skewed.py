#how to deal wirh skewed data 

#importing dependencies
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import os 

df=pd.read_csv('kc_house_data.csv')
print(df.head())

#checking the distribution of data
sns.histplot(data=df['price'],kde=True)
plt.axvline(x=df['price'].mean(),color='red',alpha=0.5,label='Mean')
plt.axvline(x=df['price'].median(),c='blue',ls='--',alpha=0.5,label='Median')
plt.legend()
print(plt.show())

#The data is right skewed


