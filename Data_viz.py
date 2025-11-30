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



