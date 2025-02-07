"""
How to put data in object?

In this section,
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("Creating new class")
print("-"*20)
# -------------


class Employee:
    pass


print("#"*40, end="\n\n")
############################

print("Creating 2 objects")
print("-"*20)
# -------------


e1 = Employee()
e2 = Employee()

print("#"*40, end="\n\n")
############################

print("Total we have 3 objects")
print("-"*20)
# -------------

# CLASS OBJECT: 'Employee': In the name of class,
#           one object will get created automatically
# INSTANCE OBJECTS: e1 & e2 which we are creating


print("#"*40, end="\n\n")
############################


print("Store Data Inside Objects")
print("-"*20)
# -------------

Employee.company_name = "XYZ Company"
# It will create new variable 'company_name' inside object and store the value
e1.name = "emp-1"
# It will create new variable 'name' inside object and store the value
e2.name = "emp-2"
# It will create new variable 'name' inside object and store the value

print("#"*40, end="\n\n")
############################

print("DATA present in each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee.company_name)
print("DATA present in instance object 'e1':", e1.name)
print("DATA present in instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
############################

print("METHODS/VARIABLES present in each objects")
print("-"*20)
# -------------

print("METHODS/VARIABLES present in class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

# -------------
# About class object 'Employee'
# -------------
# - It is common space for all INSTANCE OBJECTS
# - Data which is common for all instances can be stored in
#   class object 'Employee'
############################

"""
How to put data in object?

In this section,
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("Creating new class")
print("-"*20)
# -------------


class Employee:
    pass


print("#"*40, end="\n\n")
############################

print("Creating 2 objects")
print("-"*20)
# -------------


e1 = Employee()
e2 = Employee()

print("#"*40, end="\n\n")
############################

print("Total we have 3 objects")
print("-"*20)
# -------------

# CLASS OBJECT: 'Employee': In the name of class,
#           one object will get created automatically
# INSTANCE OBJECTS: e1 & e2 which we are creating


print("#"*40, end="\n\n")
############################


print("Store Data Inside Objects")
print("-"*20)
# -------------

Employee.company_name = "XYZ Company"
# It will create new variable 'company_name' inside object and store the value
e1.name = "emp-1"
# It will create new variable 'name' inside object and store the value
e2.name = "emp-2"
# It will create new variable 'name' inside object and store the value

print("#"*40, end="\n\n")
############################

print("DATA present in each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee.company_name)
print("DATA present in instance object 'e1':", e1.name)
print("DATA present in instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
############################

print("METHODS/VARIABLES present in each objects")
print("-"*20)
# -------------

print("METHODS/VARIABLES present in class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

# -------------
# About class object 'Employee'
# -------------
# - It is common space for all INSTANCE OBJECTS
# - Data which is common for all instances can be stored in
#   class object 'Employee'
############################