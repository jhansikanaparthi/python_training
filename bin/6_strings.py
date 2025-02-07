"""
- Strings:
        -- We have option to store text-data/collection of characters like name, email-id etc
        -- Automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("Store the values")
print("-"*20)
# -------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)"""
d = '''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)'''
e = 'PERSON\'S'

# In all the above cases builtin class 'str' object will be created and store the values

print(a, b, c, d, e, sep="\n")

print("#"*40, end="\n\n")
############################

print("Strings PART-2")
print("Store the values")
print("-"*20)
# -------------

a = "C:\newfolder\test.py"
# \n -> replace with newline
# \t -> replace with tab space
print("Value of a=", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r -> Raw string
print("Value of b=", b, end="\n\n")

print("Convert existing string 'a' to raw format:", repr(a), end="\n\n")

print("#"*40, end="\n\n")
############################

print("Strings PART-3")
print("Store the values")
print("-"*20)
# -------------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f -> format
# f -> replaces {variable_name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
############################
print("Strings PART-4")
print("Indexes: We can access each character using index")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx

print("character at index-0 using positive index:", my_string[0])
print("character at index-0 using negative index:", my_string[-8])

# print("character at index-1000 using positive index:", my_string[1000]) # ERROR

print("#"*40, end="\n\n")
############################

print("Strings PART-5")
print("Slicing: We can get substring")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx

print("substring from index-1 to 6 using positive indexes:", my_string[1:6])
print("substring from index-1 to 6 using negative indexes:", my_string[-7:-2])
print("substring from index-1 to 6 using positive/negative indexes:", my_string[1:-2])
print("substring from index-1 to 6 using positive/negative indexes:", my_string[-7:6], end="\n\n")
# ALWAYS character at start-index will be included and end-index will be excluded

print("substring from index-1 to END using positive indexes:", my_string[1:])
print("substring from index-1 to END using negative indexes:", my_string[-7:], end="\n\n")

print("substring from BEGINNING to index-6 using positive indexes:", my_string[:6])
print("substring from BEGINNING to index-6 using negative indexes:", my_string[:-2], end="\n\n")


print("#"*40, end="\n\n")
############################

print("Strings PART-6")
print('Providing step value: We can skip characters')
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx

print("substring from index-1 to 6 using positive indexes with default step value=1:", my_string[1:6])
print("substring from index-1 to 6 using negative indexes with default step value=1:", my_string[-7:-2], end="\n\n")
# default step=1: Which means from 1 to 6 give me every character

print("substring from index-1 to 6 using positive indexes with step value=1:", my_string[1:6:1])
print("substring from index-1 to 6 using negative indexes with step value=1:", my_string[-7:-2:1], end="\n\n")
# step=1: Which means from 1 to 6 give me every character

print("substring from index-1 to 6 using positive indexes with step value=2:", my_string[1:6:2])
print("substring from index-1 to 6 using negative indexes with step value=2:", my_string[-7:-2:2], end="\n\n")
# step=2: Which means from 1 to 6 give me every 2nd character

print("#"*40, end="\n\n")
############################

print("Strings PART-7")
print('Providing negative step value: Reverse order')
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx

# Example: index-1 to 6 in reverse direction
# Step-1: start index should be 6
# Step-2: end index should be 1
# Step-3: step value should be negative (here -1)
# IF WE MISS ANY STEP THEN WE WILL GET EMPTY STRING

print("substring from index-6 to 1 using positive index with step = -1:", my_string[6:1:-1])
print("substring from index-6 to 1 using negative index with step = -1:", my_string[-2:-7:-1])

print("#"*40, end="\n\n")
############################

print("METHODS present in 'str' class")
print("-"*20)
# -------------

print(dir(my_string))
# OR
# print(dir(str))

print("#"*40, end="\n\n")
############################
# why __ names?
# -------------
# - these system defined names
# - these names are already mapped to some functions or operators
#   Example: + -> __add__
#           * -> __mul__
#           len() -> __len__
#           r -> __repr__
#           f -> __format__
############################

print("Learning startswith() method")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

startswith_result = my_string.startswith("WEL") # True/False
print("startswith_result:", startswith_result)

print("#"*40, end="\n\n")
############################