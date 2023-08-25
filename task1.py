import pandas as pd
import numpy as np
import statistics as st

data = pd.read_csv("Inc_Exp_Data.csv")
data.info()
data.shape
data.describe().T
mean=data["Mthly_HH_Expense"].mean()
median=data["Mthly_HH_Expense"].median()
mode=data["Mthly_HH_Expense"].mode()
dev=st.stdev(data["Mthly_HH_Expense"])
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: "), dev