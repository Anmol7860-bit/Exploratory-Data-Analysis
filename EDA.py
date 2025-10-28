import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")
penguin=pd.read_csv('penguins_lter.csv')
print(penguin.head())
print(penguin.shape)
#delete the nan rows/columns which are not required which is done inplace
print(penguin.dropna(inplace=True))
#coloumns which are not important to your case study drop it 
a=penguin.drop(['studyName','Sample Number','Stage','Region','Individual ID','Date Egg','Delta 15 N (o/oo)','Delta 13 C (o/oo)','Comments'],axis=1)
print(a)
#nunique function to count unique values in each column 
print(a.nunique())
# drop duplicates()
print(a.drop_duplicates())
print(a.describe(include='all'))
#info function to get the information about the data types and non null values
print(a.info())
#Rename the miss spelled words or titles
a=a.rename(columns={'Clutch Completion':'Clutch_Completion','Body Mass (g)':'Body_Mass(g)'})
print(a)
#unique values in body mass coloumn to determine whether the sample size is of same size and age 
print(a.info())
BMI_Unique=a['Body_Mass(g)'].unique()
print(BMI_Unique)

#dealing with missing values

#replacing with NaN if there is any '\.+-" such values 
print(a.replace('\.+-' ,np.nan,regex=True))

print(a.isnull().sum())
print(a.head())
#reviewing each coloumn datatype
print(a.info())

#some data contains categorical values in the form of 0 or 1 to convert this into numeric we use pd.to_numeric function
a['Body_Mass(g)']=pd.to_numeric(a['Body_Mass(g)'],errors='coerce')

