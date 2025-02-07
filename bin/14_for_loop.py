"""
for-loop: Iterate any collections like string, list, tuple etc
"""

print("Iterate strings")
print("-"*20)
# -------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Value of i is:", i)

print("#"*40, end="\n\n")
############################

print("Iterate list")
print("-"*20)
# -------------

my_list = ["Java", "python", "C++"]
print("my_list:", my_list, end="\n\n")

for i in my_list:
    print("Each Value:", i)

print("#"*40, end="\n\n")
############################

print("Iterate dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for key in my_dictionary: # Iterate key
    print("Key:", key)
    print("Value:", my_dictionary[key])
    
print("#"*40, end="\n\n")
###########################

# 2 Cases
# -------------
# Case-1: 'break-statement' We can end for-loop in between
# Case-2: 'continue-statement' We can skip current iteration
#           and send it for next iteration
############################

print("# Case-1: 'break-statement' We can end for-loop in between")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# Requirement: If key 'course' found then iterating other keys are not required,
#   so end the loop

for key in my_dictionary:
    print("Key:", key)
    print("Value:", my_dictionary[key])
    if key == 'course':
        print("Since we got key='course', We are ending the loop")
        break

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

for key in my_dictionary:
    if key == 'course':
        print("\nSince we got key='course', We are sending to next iteration\n")
        continue
    print("Key:", key)
    print("Value:", my_dictionary[key])

print("#"*40, end="\n\n")
############################


print("'for-else' block")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")


for key in my_dictionary:
    print("Key:", key)
    print("Value:", my_dictionary[key])
else:
    print("After completing for-loop, this else block will execute")

# Behavior of 'else' block
# point-1: after completing for-block, else-block will execute
# point-2: if for-block ended using 'break' then break will come out of
#       'else' block as well

print("#"*40, end="\n\n")
############################

print("'for-else' block")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")


for key in my_dictionary:
    print("Key:", key)
    print("Value:", my_dictionary[key])
else:
    print("After completing for-loop, this else block will execute")

# Behavior of 'else' block
# point-1: after completing for-block, else-block will execute
# point-2: if for-block ended using 'break' then break will come out of
#       'else' block as well

print("#"*40, end="\n\n")
############################