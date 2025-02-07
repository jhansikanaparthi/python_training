"""
while-loop: We can execute loop based on condition
"""

print("while-loop example")
print("-"*20)
# -------------

x = 0
while x < 5:
    print("Value of x:", x)
    x = x + 1

print("#"*40, end="\n\n")
############################

print("while-loop with list")
print("-"*20)
# -------------

my_list = ["Java", "Python", "C++"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    print("Each Value:", my_list[index_no])
    index_no = index_no + 1

# If collections are not having indexes like set, frozenset etc,
# then convert to list/tuple and iterate using while-loop

print("#"*40, end="\n\n")
############################
# 2 Cases
# -------------
# Case-1: 'break-statement' We can end while-loop in between
# Case-2: 'continue-statement' We can skip current iteration
#           and send it for next iteration
############################

print("# Case-1: 'break-statement' We can end while-loop in between")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# Requirement: If key 'course' found then iterating other keys are not required,
#   so end the loop

# Example:
# >>> my_dictionary = {"duration":10, "course":"python", "mode":"online"}
# >>> all_keys = my_dictionary.keys()
# >>> all_keys
# dict_keys(['duration', 'course', 'mode'])
# >>> type(all_keys)
# <class 'dict_keys'>
# >>> # index numbers are not present in above collection
# >>> # so convert to list
# >>> all_keys_in_list = list(all_keys)
# >>> all_keys_in_list
# ['duration', 'course', 'mode']

all_keys = my_dictionary.keys()
all_keys_in_list = list(all_keys)
# ['duration', 'course', 'mode']

index_no = 0
while index_no < len(all_keys_in_list):
    key = all_keys_in_list[index_no]
    print("Key:", key)
    print("Value:", my_dictionary[key])
    if key == 'course':
        print("Since we got key='course', We are ending the loop")
        break
    index_no = index_no + 1

# for key in my_dictionary:
#     print("Key:", key)
#     print("Value:", my_dictionary[key])
#     if key == 'course':
#         print("Since we got key='course', We are ending the loop")
#         break

print("#"*40, end="\n\n")
############################
print("""
# Case-2: 'continue-statement' We can skip current iteration
#           and send it for next iteration
""")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# Requirement: If key 'course' found then send it to next iteration,
# because that value is not required to print

all_keys = my_dictionary.keys()
all_keys_in_list = list(all_keys)
# ['duration', 'course', 'mode']

index_no = 0
while index_no < len(all_keys_in_list):
    key = all_keys_in_list[index_no]
    if key == 'course':
        print("\nSince we got key='course', We are sending to next iteration\n")
        index_no = index_no + 1
        continue
    print("Key:", key)
    print("Value:", my_dictionary[key])
    index_no = index_no + 1


# for key in my_dictionary:
#     if key == 'course':
#         print("\nSince we got key='course', We are sending to next iteration\n")
#         continue
#     print("Key:", key)
#     print("Value:", my_dictionary[key])

print("#"*40, end="\n\n")
############################"

print("'while-else' block")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")


all_keys = my_dictionary.keys()
all_keys_in_list = list(all_keys)
# ['duration', 'course', 'mode']

index_no = 0
while index_no < len(all_keys_in_list):
    key = all_keys_in_list[index_no]
    print("Key:", key)
    print("Value:", my_dictionary[key])
    index_no = index_no + 1
else:
    print("After completing for-loop, this else block will execute")

# for key in my_dictionary:
#     print("Key:", key)
#     print("Value:", my_dictionary[key])
# else:
#     print("After completing for-loop, this else block will execute")

# Behavior of 'else' block
# point-1: after completing for-block, else-block will execute
# point-2: if for-block ended using 'break' then break will come out of
#       'else' block as well

print("#"*40, end="\n\n")
############################