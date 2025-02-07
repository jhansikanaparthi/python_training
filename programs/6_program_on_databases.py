"""
Get data from web_server.log

then

extract using regular expression
IP
DATE
URL

then

send extracted data to database
"""

"""
How to communicate with databases in python?

python-program  <-- using library -->  any databases(SQL/No-SQL)

Example:
python-program  <-- using library (cx-oracle) -->  oracle databases
python-program  <-- using library (mysql.connector) -->  mysql databases
python-program  <-- using library (sqlite3) -->  SQLite databases
"""

"""
We need ONE database..
- We can use SQLite database
- lightweight database
- SQLite database is not running any server
- It will create sqlite database file
- on that sqlite database file, we can SQL query
"""

"""
How to create and communicate with SQLite database?

2 ways:
1-way: Using SQLite database software
2-way: WITHOUT Using SQLite database software,
        USING python library sqlite3, we can create database
        and communicate with database
"""

print("Creating database and table")
print("-"*20)
# -------------

import sqlite3

print("Creating/connecting to database 'my_database.db'")
my_db_connection = sqlite3.connect("my_database.db")
print("Done\n")


print("Create cursor object in order execute sql queries")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
URL VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")

print("#"*40, end="\n\n")
############################

print("Get data from web_server.log")
print("-"*20)
# -------------

my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
############################

print("Extract IP, DATE, URL")
print("-" * 20)
# -------------

import re

for each_line in log_file_content:
    match_result = re.match(
        r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}', '{url}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records are inserted. Please check DB")

print("#" * 40, end="\n\n")
############################
print("Executing Select Query")
print("-" * 20)
# -------------

my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
print("my_db_result:", my_db_result)
my_db_connection.close()
print("DB Connection closed")

print("#" * 40, end="\n\n")
############################