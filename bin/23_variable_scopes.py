"""
Here,
Scope-3: Global Scope


"""

print("Scope-3: Global Scope CASE-1")
print("-"*20)
# -------------

x = 100 # In Global Scope, We can access any-where/any-block


def my_function():
    print("Accessing global variable inside my-function:", x)


my_function()
print("Outside the function, value of x is:", x)


print("#"*40, end="\n\n")
############################


print("Scope-3: Global Scope CASE-2")
print("-"*20)
# -------------

x = 100 # In Global Scope, We can access any-where/any-block


def my_function():
    # x = 200 # It will create local variable
    global x # refers global variable
    x = 200 # It will update global varaible x
    print("Accessing global variable inside my-function:", x) # 200


my_function()
print("Outside the function, value of x is:", x) # 200


print("#"*40, end="\n\n")
############################