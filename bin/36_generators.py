"""
Generators: We can generate object whenever we want or on-the-fly
"""

print("WITHOUT Using Generators")
print("-"*20)
# -------------


def my_square_function(my_list):
    result = []
    for i in my_list:
        result.append(i*i)
    return result


L = [10, 20, 30, 40]
square_result = my_square_function(L)
print("square_result:", square_result, end="\n\n")

for i in square_result:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
############################

print("USING Generators")
print("-"*20)
# -------------


def my_square_function(my_list):
    for i in my_list:
        yield i * i

L = [10, 20, 30, 40]
square_result = my_square_function(L)
print("square_result:", square_result, end="\n\n")

for i in square_result:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
############################

print("Other way to create generator object: tuple comprehension")
print("-"*20)
# -------------

# LIST/TUPLE/DICTIONARY/SET COMPREHENSION: We can write expression in LIST/TUPLE/DICTIONARY/SET

L = [10, 20, 30, 40]
my_squared_list = [i*i for i in L]
print("my_squared_list:", my_squared_list, end="\n\n")

my_squared_tuple = (i*i for i in L)
print("my_squared_tuple:", my_squared_tuple, end="\n\n")

print("Iterating from my_squared_tuple generator")
for i in my_squared_tuple:
    print("Value of i:", i*i)

print("#"*40, end="\n\n")
############################