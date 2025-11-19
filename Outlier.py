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