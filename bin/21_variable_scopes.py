"""
4 Scopes

Scope-1: Local Scope
Scope-2: Enclosed Scope
Scope-3: Global Scope
Scope-4: Builtin
If nowhere found in the current program,
It will go and check in builtins
Scope-4: Builtin

"""

print("Scope-1: Local Scope")
print("-"*20)
# -------------


def my_function():
    x = 100 # Local Scope, We can't access outside the function
    print("Inside function, Value of x is:", x)


my_function()

print("#"*40, end="\n\n")
############################