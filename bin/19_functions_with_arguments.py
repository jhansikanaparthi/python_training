"""
Here,
Case-2: How to pass values to variables present inside the function

Functions with arguments:

3 ways to pass values to variables present inside the function
1-way: We can pass ONLY VALUES or ARG_NAME=VALUE format
    called POSITIONAL or KEYWORD argument function
2-way: We can RESTRICT to pass ONLY VALUES
    called POSITIONAL ONLY argument function
3-way: We can RESTRICT to pass only ARG_NAME=VALUE format
    called KEYWORD ONLY argument function
"""

print("""
1-way: We can pass ONLY VALUES or ARG_NAME=VALUE format
    called POSITIONAL or KEYWORD argument function
""")
print("-"*20)
# -------------

# name, company are called POSITIONAL or KEYWORD arguments
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# WE CAN PASS ONLY VALUES
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# OR WE CAN PASS in ARG_NAME=VALUE format
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("""
2-way: We can RESTRICT to pass ONLY VALUES
    called POSITIONAL ONLY argument function
""")
print("-"*20)
# -------------

# / -> is just syntax to tell it is only positional argument function
# / -> not counted as argument
# / -> We are not passing any values to /

# name, company are called POSITIONAL arguments
def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# WE CAN PASS ONLY VALUES
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# BELOW CODE WILL NOT WORK
# OR WE CAN PASS in ARG_NAME=VALUE format
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("""
3-way: We can RESTRICT to pass only ARG_NAME=VALUE format
    called KEYWORD ONLY argument function
""")
print("-"*20)
# -------------

# * -> is just syntax to tell it is only keyword argument function
# * -> not counted as argument
# * -> We are not passing any values to *

# name, company are called KEYWORD arguments
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# BELOW CODE WILL NOT WORK
# WE CAN PASS ONLY VALUES
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

# OR WE CAN PASS in ARG_NAME=VALUE format
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################