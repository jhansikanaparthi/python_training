"""
Functions with variable arguments
1. Functions with variable positional arguments
2. Functions with variable keyword arguments
"""

print("1. Functions with variable positional arguments")
print("-"*50)
# -------------

# * -. syntax
# *a -> variable argument which takes 0 or more values
def x(*a):
    print("Received Values In Tuple:", a)

x()
x(10)
x(10, 20, 30)

print("#"*40, end="\n\n")
############################

print("2. Functions with variable keyword arguments")
print("-"*20)
# -------------

# ** -> is just syntax
# **a -> variable keyword arguments
def y(**a):
    print("Received Values In Dictionary:", a)


y()
y(name="emp-1")
y(name="emp-2", email="a@b.com", phone="111111")

print("#"*40, end="\n\n")
############################