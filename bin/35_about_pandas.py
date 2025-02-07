"""
About pandas (FOR TABULAR DATA PROCESSING like csv/excel/db etc)
- pandas is one library
- pandas has many functions and classes
- Few function names are read_csv, read_excel, read_sql many more
- Few class names are DataFrame, Series and many more

About 'DataFrame'
- 'DataFrame' class is MAIN class here
- 'DataFrame' class written for tabular data processing
- 'DataFrame' class has many matheatical methods like
    sum(), std(), mean() etc

    and other methods like: to_csv, to_excel

"""
print("Inside pandas library")
print("-"*20)
# -------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
############################

print("Inside DataFrame class")
print("-"*20)
# -------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
############################

print("DataFrame example - 1")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
############################

print("DataFrame example - 2")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]],
                     index=["r1", "r2"],
                     columns=["c1", "c2", "c3"]
                     )
print(my_df)

print("#"*40, end="\n\n")
############################