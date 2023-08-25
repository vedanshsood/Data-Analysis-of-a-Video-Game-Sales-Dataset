# importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the csv file
data=pd.read_csv("Tasks Data Science\Games_dataset.csv")
data.info()
data.shape
data.describe().T

#Mean
mean=data["Global_Sales"].mean()
#Median
median=data["Global_Sales"].median()
#Mode
mode=data["Global_Sales"].mode()
#Standard Deviation
dev=np.std(data["Global_Sales"])
# Printing the desprictive Analysis
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: ",dev )

#Creating Histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(data["Global_Sales"], bins = [0, 8, 16, 24, 32, 40, 48, 56, 64])

#Showing the plot
plt.show()