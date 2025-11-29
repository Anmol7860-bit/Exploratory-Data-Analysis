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
#Data transformation is the process of talking a mathematical function and applying it to data
#Types of transformation 
#1. Log Transformation 
# Each variable x is replaced with log(x) normally log base or natural log is used 
# The log transformation can be used to make skewed distribution less skewed 
# This can be valuable both for making patterns in the data more interpretable and to meet the assumptiions of inferential statistics 
df['price_log']=np.log(df['price'])
sns.histplot(data=df['price_log'],kde=True)
print(plt.show())

#2. Square root transformation 
#Normalizing a skewed distribution 
#Reducing heteroscedasticity of the residuals in linear regression 
#focusing on visualizing certain parts of your data 
#when you apply square root transformation to a variable.high values compressed and low values become spread out. log transformation does the same thing but more aggressively 

df['price_sqrt']=np.sqrt(df['price'])
sns.histplot(data=df['price_sqrt'],kde=True)
plt.axvline(x=df['price_sqrt'].mean(),color='red',alpha=0.5,label='Mean')
plt.axvline(x=df['price_sqrt'].median(),c='blue',ls='--',alpha=0.5,label='Median')
plt.legend()
print(plt.show())

#3. power or box cox transformation
#The Box-Cox transformation is a family of power transformations that are designed to stabilize variance and make the data more closely conform to a normal distribution.
#A power transform is a family of functions applied to create a monotonic transformation of data using power functions 

from scipy.stats import boxcox
df.insert(len(df.columns),'A_boxcox',boxcox(df['price'])[0])
sns.histplot(data=df['A_boxcox'],kde=True)
print(plt.show())