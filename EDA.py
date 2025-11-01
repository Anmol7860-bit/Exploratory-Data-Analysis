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
penguin=penguin.drop(['studyName','Stage','Region','Individual ID','Date Egg','Delta 15 N (o/oo)','Delta 13 C (o/oo)','Comments'],axis=1)
print(penguin)
#nunique function to count unique values in each column 
print(penguin.nunique())
# drop duplicates()
print(penguin.drop_duplicates())
print(penguin.describe(include='all'))
#info function to get the information about the data types and non null values
print(penguin.info())
#Rename the miss spelled words or titles
penguin=penguin.rename(columns={'Clutch Completion':'Clutch_Completion','Body Mass (g)':'Body_Mass(g)'})
print(penguin)
#unique values in body mass coloumn to determine whether the sample size is of same size and age 
print(penguin.info())
BMI_Unique=penguin['Body_Mass(g)'].unique()
print(BMI_Unique)

#dealing with missing values

#replacing with NaN if there is any '\.+-" such values 
print(penguin.replace('\.+-' ,np.nan,regex=True))

print(penguin.isnull().sum())
print(penguin.head())
#reviewing each coloumn datatype
print(penguin.info())

#some data contains categorical values in the form of 0 or 1 to convert this into numeric we use pd.to_numeric function
penguin['Body_Mass(g)']=pd.to_numeric(penguin['Body_Mass(g)'],errors='coerce')
# find ambiguity in the data
print(penguin.describe(include='all'))
#check if the body mass coloumn contain 0 valuse as body mass is always greater than zero
print(penguin['Body_Mass(g)']==0)

#lets plot this data for a wider picture
sns.histplot(data=penguin['Body_Mass(g)'],kde=True)
plt.axvline(x=penguin['Body_Mass(g)'].mean(),color='red',alpha=0.5,label='Mean')
plt.axvline(x=penguin['Body_Mass(g)'].median(),c='blue',ls='--',alpha=0.5,label='Median')
plt.legend()
#print(plt.show())

#the picture shows the mean median values and data plotted as histogram
#if the body mass column contains the values 0 then convert it into nan because body mass of any object cannot be zero
penguin['Body_Mass(g)'] = penguin['Body_Mass(g)'].replace(0, np.nan)#there are no o values
print(penguin['Body_Mass(g)'])

#Analysing the amount of missing values
penguin_missing=penguin.isnull()
print(penguin_missing) #no missing value found

#total missing values in each coloumn
print(penguin.isnull().sum())

#percentage of missing values in each coloumn
print(penguin.isnull().mean()*100)

#visualising the missing data using missingno library
import missingno as msno
print(msno.bar(penguin))
