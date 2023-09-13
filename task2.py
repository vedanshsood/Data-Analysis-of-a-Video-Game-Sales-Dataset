# importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Pearson Correlation Coefficient
def pearson(x,y):
    pearson = np.corrcoef(x,y)
    return pearson


# Reading the csv file
data=pd.read_csv("Tasks Data Science\Games_dataset.csv")
data.info()
data = pd.DataFrame(data)

#printing data
print(data)

# Descriptive Analysis of the data 
print(data.describe())


#Creating Histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(data["Global_Sales"], bins = [0, 8, 16, 24, 32, 40, 48, 56])

#Showing the plot
plt.show()

#Calculating Pearson correlation coefficient for North America Sales and Global Sales
correlation = pearson(data["NorthAmerica_Sales"],data['Global_Sales'])
print("The Pearson Correlation Coefficient is: ")
print(correlation)


# Finding Null values in the data 
print(data.isnull().sum())

#Removing string columns
data1 = data.drop(["Name","Platform","Year" , "Genre","Publisher"] , axis = 1)
data1.head()

# Correlation matrix
relation = data1.corr()
sns.heatmap(relation, xticklabels=relation.columns , yticklabels=relation.columns , annot=True)

plt.show()

#Data visualisation for the sales of video games
sns.pairplot(relation)
plt.show()

#Scatter plot
sns.relplot(x="NorthAmerica_Sales", y="Japan_Sales", hue="Genre", data= data)
plt.show()