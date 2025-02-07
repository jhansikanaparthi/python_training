"""
Problem Statement:

Get data from below files
1. practice/log_report_1.json
2. practice/log_report_2.json
3. my_database.db

produce single report
final_report.csv
final_report.xlsx
final_report.json
final_report.xml
"""

print("Get data from 'practice/log_report_1.json'")
print("-"*20)
# -------------

import pandas as pd
my_json_file_data_1 = pd.read_json(r"C:\python_training\log_report_1.json")
print(my_json_file_data_1)

print("#"*40, end="\n\n")
############################
print("Get data from 'practice/log_report_2.json'")
print("-"*20)
# -------------

import pandas as pd
my_json_file_data_2 = pd.read_json(r"C:\python_training\log_report_2.json")
print(my_json_file_data_2)

print("#"*40, end="\n\n")
############################


print("ROTATING my_json_file_data_2 data")
print("-"*20)
# -------------

my_json_file_data_2 = my_json_file_data_2.T # Transpose-> Rotate
print(my_json_file_data_2)

print("#"*40, end="\n\n")
############################

print("Get data from database")
print("-"*20)
# -------------

import sqlite3
my_db_connection = sqlite3.connect("my_database.db")

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)

print(my_db_df)

print("#"*40, end="\n\n")
############################

print("Changing Column Names")
print("-"*20)
# -------------

print("my_json_file_data_1 - Current column names:", my_json_file_data_1.columns, sep="\n", end="\n\n")
print("my_json_file_data_2 - Current column names:", my_json_file_data_2.columns, sep="\n", end="\n\n")
print("my_db_df - Current column names:", my_db_df.columns, sep="\n", end="\n\n")

# ['IP', 'DATE', 'URL']

my_json_file_data_1.columns = ['IP', 'DATE', 'URL']
print("After changing column name, my_json_file_data_1 - Current column names:", my_json_file_data_1.columns, sep="\n", end="\n\n")

my_json_file_data_2.columns = ['IP', 'DATE', 'URL']
print("After changing column name, my_json_file_data_2 - Current column names:", my_json_file_data_2.columns, sep="\n", end="\n\n")

print("my_db_df - Current column names:", my_db_df.columns, sep="\n", end="\n\n")


print("#"*40, end="\n\n")
############################


print("Merge All")
print("-"*20)
# -------------

# my_json_file_data_1
# my_json_file_data_2
# my_db_df

all_in_one_df = pd.concat([my_json_file_data_1, my_json_file_data_2, my_db_df], axis=0)
# axis=0 -> One below the other
# axis=1 -> One after the other
print(all_in_one_df)

print("#"*40, end="\n\n")
############################

print("Write to files")
print("-"*20)
# -------------

# all_in_one_df = all_in_one_df.drop_duplicates()

# final_report.csv
all_in_one_df.to_csv("final_report.csv", index=None)

# final_report.xlsx
all_in_one_df.to_excel("final_report.xlsx", index=None)

# final_report.xml
all_in_one_df.to_xml("final_report.xml")

print("""
Created below files,
 
final_report.csv
final_report.xlsx
final_report.xml

please check
""")

print("#"*40, end="\n\n")
############################

print("Reset index numbers")
print("-" * 20)
# -------------

all_in_one_df = all_in_one_df.reset_index(drop=True)
# drop=True # Remove existing index column
print(all_in_one_df)


print("#" * 40, end="\n\n")
############################

print("Create json file")
print("-" * 20)
# -------------

all_in_one_df.to_json("final_report_1.json")

all_in_one_df = all_in_one_df.T
all_in_one_df.to_json("final_report_2.json")

print("""
Created

final_report_1.json
final_report_2.json

please check
""")
print("#" * 40, end="\n\n")
############################