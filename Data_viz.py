import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


gapminder=pd.read_csv('gapminder_data_graphs.csv')
print(gapminder.head())

#Examining Categorical-Numerical data
#we can use Box plot to visualize the distribution of a numerical variable across different categories of a categorical variable
plt.figure(figsize=(10,6))
sns.boxplot(x='continent',y='life_exp',data=gapminder)
plt.title('Life Expectancy by Continent')
plt.show()

#bar plot
plt.figure(figsize=(10,6))
sns.barplot(x='continent',y='life_exp',data=gapminder,color='teal')
plt.title('Life Expectancy by Continent')
plt.show()

#Examining Numerical-Numerical data
#We can use scatter plot to visualize the relationship between two numerical variables
#Scatter plot tells us how the data points are distributed and whether there is any correlation between the two variables
#Try to make non linear relationships between variables, linear using transformation outliers and skewness techniques
gapminder_2007=gapminder[gapminder['year']==2007]
plt.figure(figsize=(10,6))
sns.scatterplot(x='gdp',y='life_exp',data=gapminder_2007,hue='continent')
plt.title('Life Expectancy vs GDP per Capita')
plt.xlabel('Gdp per capita')
plt.ylabel('Life Expectancy')
plt.show()

#we are converting gdp column into log scale
sns.scatterplot(x='gdp',
                y='life_exp',
                data=gapminder_2007,)
plt.xscale('log')
plt.title('Life Expectancy vs GDP per Capita (Log Scale)')
plt.xlabel('Gdp per capita (Log Scale)')
plt.ylabel('Life Expectancy')
plt.show()

#Examining Numerical-Numerical data to see the trend 
gapminder_India=gapminder[gapminder['country']=='India']
plt.figure(figsize=(10,6))
sns.lineplot(x='year',y='life_exp',data=gapminder_India)
plt.show()

#when we are seeing the trend we create line plot 
#when we trying to see the relationship we create scatterplot

#Examining Categorical-Categorical data
data_url='https://bit.ly/3aYBbhQ'
A_data=pd.read_csv(data_url)
print(A_data.head())

#how one variable is affecting the dependent variable 
sns.countplot(x='Education',hue='Gender',data=A_data)
plt.show()

#Pairplot
iris=sns.load_dataset('iris')
g=sns.pairplot(iris,hue='species')
plt.show()

#pearson correlation heat map
#lower the value the lighter the color of the plot higher the value the darker thr color of the plot 
#ligher color means low correlation darker color means high correlation
KC=pd.read_csv('kc_house_data.csv')
KC=KC.iloc[1:]#removing first row
KC=KC.drop(['date'],axis=1)
AAA=KC.corr(method='pearson')#finding correlation between different numerical variables pearson approach(parametric approach) should not be having outliers in the dataset
plt.figure(figsize=(10,6))
heatmap=sns.heatmap(AAA,annot=True)#annot=True means show the values in the heatmap
plt.title('Correlation Heatmap')
plt.show()

#spearman correlation heatmap
#not bound with parametric assumptions
AAA.corr(method='spearman')#selecting the method as spearman
plt.show()

#Multicollinearity heatmap
sns.heatmap(AAA.corr(method='spearman'),annot=True)
plt.title('Multicollinearity Heatmap')
plt.show()
