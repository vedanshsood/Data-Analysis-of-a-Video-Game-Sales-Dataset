import pandas as pd
import numpy as np



data=pd.read_csv("Tasks Data Science\Games_dataset.csv")
data.info()
data.shape
data.describe().T
mean=data["Global_Sales"].mean()
median=data["Global_Sales"].median()
mode=data["Global_Sales"].mode()
dev=np.std(data["Global_Sales"])
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: ",dev )