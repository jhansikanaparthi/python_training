"""
About print-function
"""

print("print function using 'sep' argument")
print("-"*20)
# -------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # default sep=SPACE, In output, it will print each value separated by SPACE
print(a, b, c, d, sep="\t\t")
print(a, b, c, d, sep="XYZ")

print("#"*40, end="\n\n")
############################
print("print function using 'end' argument")
print("-"*20)
# -------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # Default end="\n", In output, after printing all the values put \n
print(a, b, c, d, end="\n\n")
print(a, b, c, d, end="XYZ\n")

# One more argument, 'file' can be passed
# This we will discuss during file operations

print("#"*40, end="\n\n")
############################