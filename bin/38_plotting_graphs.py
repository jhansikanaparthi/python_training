"""
Seaborn: Plotting graphs
"""

print("Get data from Iris.csv")
print("-"*20)
# -------------

import pandas as pd
iris_data_df = pd.read_csv("C:/python_training/bin/Iris.csv")
print(iris_data_df)

print("#"*40, end="\n\n")
############################

print("Plotting violinplot")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.violinplot(data=iris_data_df, x='Species', y='SepalLengthCm')

plt.show()

print("#"*40, end="\n\n")
############################

print("Plotting lineplot")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(data=iris_data_df, x='Species', y='SepalLengthCm')

plt.show()

print("#"*40, end="\n\n")
############################