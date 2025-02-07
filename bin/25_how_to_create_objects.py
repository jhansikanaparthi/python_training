"""
How to create or obtain objects?
- ANSWER: Using CLASSES we can create n number of objects

In this section,
1. CLASS OBJECT
2. INSTANCE OBJECT
"""

print("Creating new class")
print("-"*20)
# -------------


class Employee:
    pass

# pass -> is just DUMMY keyword
# pass -> use to keep any block empty

# Above 'Employee' class is valid class eventhugh it is empty.
# Which means, we can create objects, we can store data BUT we don't have methods

print("#"*40, end="\n\n")
############################

print("Creating 2 objects")
print("-"*20)
# -------------


e1 = Employee()
# It will create new object and store in e1
e2 = Employee()
# It will create new object and store in e2


print("#"*40, end="\n\n")
############################

print("Total we have 3 objects")
print("-"*20)
# -------------

# CLASS OBJECT: 'Employee': In the name of class,
#           one object will get created automatically
# INSTANCE OBJECTS: e1 & 2 which we are creating


print("#"*40, end="\n\n")
############################


print("DATA present in each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee)
print("DATA present in instance object 'e1':", e1)
print("DATA present in instance object 'e2':", e2)

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

# About 'object' class
# -------------
# - It is MASTER class
# - It has basic methods like construting objects, initializing objects
#   etc
# - By default, whatever there in object class, will come to
#   all other classes including builtin-class/our-class
#   - This is called INHERITANCE
#   - other-way to say, all the classes are INHERITED from 'object'
############################