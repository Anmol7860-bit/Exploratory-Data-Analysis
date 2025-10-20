import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")
penguin=pd.read_csv('penguins.csv')
print(penguin.head())
print(penguin.shape)
#delete the nan values/columns which are not required 
print(penguin.dropna(inplace=True)) 
#coloumns which are not important to your case study drop it 
a=penguin.drop(['year','sex'],axis=1)
print(a)
#nunique function to count unique values in each column 
print(a.nunique())
# drop duplicates()
print(a.drop_duplicates())
print(a.describe(include='all'))
#info function to get the information about the data types and non null values
#print(a.info())
print(a.rename(columns={'species':'Species','island':'Island'}))
BMI_unique=a.body_mass_g.unique()
#print(BMI_unique)

#dealing with missing values
#replacing with NaN
a=a.replace('\.+-',np.nan,regex=True)
print(a.isnull().sum())
print(a.head())