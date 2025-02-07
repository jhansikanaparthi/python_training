"""
- list:
        -- We have option to store multiple values like list names etc
        -- Here, we can store DUPLICATE values
        -- Automatically index number will be assigned to each value
"""

print("list PART-1")
print("Store multiple values")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
# Internally it will create object of 'list' class and store the values
print("my_list:", my_list)

print("#"*40, end="\n\n")
############################

print("list PART-2")
print("Indexes are similar to strings")
print("-"*20)
# -------------

print("1st Value:", my_list[0])
print("2nd Value:", my_list[1])

print("#"*40, end="\n\n")
############################


print("list PART-3")
print("METHODS present in 'list' class")
print("-"*20)
# -------------

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
############################

print("list PART-4")
print("count and index method")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

count_of_python = my_list.count("python") # 1
index_of_python = my_list.index("python") # 2

print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)

print("#"*40, end="\n\n")
############################

print("list PART-5")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

# ADD
my_list.append("Java")
print("my_list after appending Java:", my_list, end="\n\n")
# [10, 12.5, "python", (100, 200), Java]

# UPDATE
my_list[1] = "C++"
print("my_list after Updating to C++:", my_list, end="\n\n")
# [10, C++, "python", (100, 200), Java]

# REMOVE
my_list.pop(3)
print("my_list after deleting nested tuple:", my_list, end="\n\n")
# [10, C++, "python", Java]

print("#"*40, end="\n\n")
############################