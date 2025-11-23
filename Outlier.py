#import libraries 
import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
from scipy import stats

warnings.filterwarnings("ignore")
diabetes=pd.read_csv('diabetes.csv')
print(diabetes.head())

#first and foremost visualize the data to understand the distribution of data
sns.histplot(data=diabetes['Age'],kde=True)
plt.axvline(x=diabetes['Age'].mean(),color='red',alpha=0.5,label='Mean')
plt.axvline(x=diabetes['Age'].median(),c='blue',ls='--',alpha=0.5,label='Median')
plt.legend()
#plt.show()

sns.boxplot(y=diabetes['Age'])
#plt.show()

#Approaches can be used 
#1.outlier replacement using computed mean 
#2.outlier replacement using computed median
#3.outlier replacement using grouped mean if classification approach
#4.outlier replacement using grouped median if classification approach
#5.outlier removal or filling of missing values(Z score and/or IQR)

#Z-score method
#basically calculating standard normal distribution 
#describes any data point by finding their relationship between mean and standard deviation 
#It finds the distribution of data where mean is 0 and standard deviation is 1 
#if Z-score value is greater than 3 or -3 respectively that data point is considered as outlier 

z = np.abs(stats.zscore(diabetes['Age']))
print(z)

threshold= 3
print(np.where(z>3))

threshold=-3
print(np.where(z<-3))

#IQR method
#data has been divided into quartiles(q1,q2,q3)
#25th percentile of the data-Q1
#50th percentile of the data-Q2(median)
#75th percentile of the data-Q3
#lower limit for outliers are Q1-1.5*IQR
#upper limit for outliers are Q3+1.5*IQR
#IQR=Q3-Q1
#for extreme outliers use 3*IQR instead of 1.5*IQR


Q1=np.percentile(diabetes['Age'],25,interpolation='midpoint')
Q2=np.percentile(diabetes['Age'],50,interpolation='midpoint')
Q3=np.percentile(diabetes['Age'],75,interpolation='midpoint')

IQR=Q3-Q1
print('Interquartile range is ',IQR)
low_lim=Q1-1.5*IQR
up_lim=Q3+1.5*IQR
print('low_limit is',low_lim)
print("up_lim",up_lim)
outliers=[]
for x in diabetes['Age']:
    if (x>up_lim)or (x<low_lim):
        outliers.append(x)
print('outlier values are',outliers)


#the data now can be normal distributed
