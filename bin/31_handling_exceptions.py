"""
Exceptions Handling
"""

# print("WITHOUT Handling Exceptions")
# print("-"*20)
# # -------------
#
# a = 10
# b = 0
# result = a / b # Program will terminate abruptly
# print("result:", result)
#
# print("#"*40, end="\n\n")
# ############################

print("Handling Exceptions using 'try-except'")
print("-"*20)
# -------------

try:
    pass # If some error then execute 'except' block
            # else skip 'except' block
except:
    pass # Here, we will write logic solve problem happened in try-block

try:
    a = 10
    b = 0
    result = a / b # Program will terminate abruptly
    print("result:", result)
except:
    print("Reached 'except' block")
    print("Some error in try-block")

print("#"*40, end="\n\n")
############################

# About 'Exception' classes
# -------------
# - If we want to handle exception using 'try-except'
#   then we need to have exception-class.
#   else we can't handle so program will terminate abruptly
#
# - some exception classes are present in builtins
# - class 'Exception' is super class
############################

print("Handling Exceptions using 'try-except with class names'")
print("-"*20)
# -------------

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate here,
    # instead control will be passed to 'except' block
    print("result:", result)
except ZeroDivisionError: # 1-way to specify class name
    print("This is ZDE block")
except NameError as ne: # 2-way where we store error object
    print("This is NE block and value of ne is:", ne)
except Exception as e: # We can receive any type of exception
    print("This is 'Exception' block. Value of e is:", e)


print("#"*40, end="\n\n")
############################

print("try-except-else-finally blocks")
print("-"*20)
# -------------

try:
    print("Reached try")
    my_file_handle = open(r"D:\some_wrong_dir\test.py", "w")
except Exception as e:
    print("Reached except")
    print("Here we are handling error produced open function")
else:
    print("Reached 'else' block")
    my_file_handle.write("Hello")
    my_file_handle.write("Hi")
    my_file_handle.write("HelloHi")
finally:
    print("Reached finally")
    try:
        my_file_handle.close()
        print("File handle closed")
    except Exception as e:
        print("Not able to close file handle, Reason:", e)


# About 'else' block
# - We can say, 'else' block is continuation of 'try'
# - if 'try' success then 'else' will execute
# - if 'try' failed then 'else' will NOT execute

# About
# - if try/except/else suceess/failed. BUT finally block will always execute

print("#"*40, end="\n\n")
############################
print("User defined exception class example-1:")
print("-"*20)
# -------------

# Mandatory Step: our class should be sub-class of 'Exception' class
# OR if some classes like builtin exception classes are sub class of Exception,
#   So we can make use of that class as well


class MyError(Exception):
    pass
# It is valid Exception class
#   which means, we can make use of this class to handle 'Exception'

try:
    x = 10
    if x == 10:
        raise MyError
    if x > 10:
        raise MyError
    if x < 10:
        raise MyError
except MyError:
    print("Reached MyError except block")


print("#"*40, end="\n\n")
############################
print("User defined exception class example-2:")
print("-"*20)
# -------------

# Requirement: While raising exception, we can pass some message about


class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg

try:
    x = 10
    if x == 10:
        raise MyError("Here value of x is 10 so raising MyError")
    if x > 10:
        raise MyError("Here value of x is gt 10 so raising MyError")
    if x < 10:
        raise MyError("Here value of x is lt 10 so raising MyError")
except MyError as me:
    print("Reached MyError except block and details:", me.error_message)


print("#"*40, end="\n\n")
############################