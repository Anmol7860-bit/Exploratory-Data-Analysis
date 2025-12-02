#Binning
#To reduce the noice we bin the dataset into numerical and categorical variables
#Numerical                                   Categorical
#Age(0-18,19-35,36-60,60+)                   Age
#Salary(0-30k,30k-60k,60k-100k,100k+)        Salary
#To reduce overfitting we use binning technique
#Increases the robustness of the model

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os
penguin=pd.read_csv('penguins_lter.csv')
print(penguin.head())
#Binning the body mass column into
bins=[0,2500,4000,6000]
labels=['Low','Medium','High']
penguin['Body_Mass_Category']=pd.cut(penguin['Body Mass (g)'],bins=bins,labels=labels)
print(penguin[['Body Mass (g)','Body_Mass_Category']].head(10))
#visualizing the binned data
sns.countplot(x='Body_Mass_Category',data=penguin)
plt.title('Body Mass Category Distribution')
plt.show()

#Dummy variables
#Converting categorical variables into numerical variables
#1.Here we use pd.get_dummies() function to convert categorical variables into numerical variables
dummy_species=pd.get_dummies(penguin['Species'],prefix='Species',drop_first=True)
print(dummy_species.head())
#2.Concatenate the dummy variables with the original dataframe
penguin=pd.concat([penguin,dummy_species],axis=1)
print(penguin.head())
#3.Drop the original categorical variable
penguin=penguin.drop('Species',axis=1)
print(penguin.head())
#Now the penguin dataframe contains numerical variables only
#This can be used for machine learning models which require numerical input

#Label Encoding
#Another way to convert categorical variables into numerical variables
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
penguin['Island_Encoded']=le.fit_transform(penguin['Island'])
print(penguin[['Island','Island_Encoded']].head())
#Here the Island column is converted into numerical values
#Each unique category is assigned a unique integer value
#This can also be used for machine learning models which require numerical input
#Note: Label encoding is suitable for ordinal categorical variables where the categories have a meaningful order
#For nominal categorical variables(one without order) use one hot encoding(pd.get_dummies())
print(le.classes_)
#To decode back the numerical values to original categorical values
decoded_island=le.inverse_transform(penguin['Island_Encoded'])
print(decoded_island[:5])

#Feature Scaling
#adjusting the range of features to a standard scale
#Is the step of data preprocessing that aims to standardize the range of independent variables or features of data
#Normalization (Min-Max Scaling) to normalize the data between 0 and 1 normalized_value=(x-min)/(max-min)
#Normalization is on 0 and 1 scale and is heavily affected by outliers 
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
penguin[['Culmen Length (mm)','Culmen Depth (mm)']]=scaler.fit_transform(penguin[['Culmen Length (mm)','Culmen Depth (mm)']])
print(penguin[['Culmen Length (mm)','Culmen Depth (mm)']].head())   


#Standardization (Z-score Scaling) standardized_value=(x-mean)/std_dev
#Standardization is not bounded to a specific range and is less affected by outliers
#It centers the data around 0 with a standard deviation of 1
from sklearn.preprocessing import StandardScaler
std_scaler=StandardScaler()
penguin[['Flipper Length (mm)','Body Mass (g)']]=std_scaler.fit_transform(penguin[['Flipper Length (mm)','Body Mass (g)']])
print(penguin[['Flipper Length (mm)','Body Mass (g)']].head())

