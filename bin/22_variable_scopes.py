"""
Here,
Scope-2: Enclosed Scope


"""

print("Scope-2: Enclosed Scope CASE-1")
print("-"*20)
# -------------


def my_function_1():
    x = 100 # Enclosed Scope: CURRENT and NESTED function can access

    def my_function_2():
        nonlocal x
        print("Accessing function_1 variable x in function_2 and its value:", x) # 100
    my_function_2()
    print("In function_1, Value of x is:", x) # 100


my_function_1()


print("#"*40, end="\n\n")
############################


print("Scope-2: Enclosed Scope CASE-2")
print("-"*20)
# -------------


def my_function_1():
    x = 100 # Enclosed Scope: CURRENT and NESTED function can access

    def my_function_2():
        # x = 200 # It will create local variable
        nonlocal x # This refers outer function x
        x = 200 # This will change outer function x value to 200
        print("Accessing function_1 variable x in function_2 and its value:", x) # 200
    my_function_2()
    print("In function_1, Value of x is:", x) # 200


my_function_1()


print("#"*40, end="\n\n")
############################