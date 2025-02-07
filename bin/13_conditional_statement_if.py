"""
Conditional Statement 'if': We can execute block code based on the condition
"""
print("Only if blocks")
print("-"*20)
# -------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")
print("This is not inside the block")

if x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

if x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
############################

print("if-elif blocks")
print("-"*20)
# -------------

x = 4
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")
print("This is not inside the block")


print("#"*40, end="\n\n")
############################
print("if-elif-else blocks")
print("-"*20)
# -------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")
print("This is not inside the block")


print("#"*40, end="\n\n")
############################

print("if block with str, list, tuple etc")
print("-"*20)
# -------------

my_string = "Python"
my_list = ["Java", "C", "C++"]

print("my_string:", my_string)
print("my_list:", my_list, end="\n\n")

if ("tho" in my_string) and (my_string != "Java") and ("C++" in my_list):
    print("All are True")

print("#"*40, end="\n\n")
############################

print("if block with dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['duration', 'course', 'mode']
# >>>
if "duration" in my_dictionary.keys():
    print("Key 'duration' found")

# >>> my_dictionary.values()
# [10, 'python', 'online']
# >>>
if 'python' in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('duration', 10), ('course', 'python'), ('mode', 'online')]
# >>>
if ('duration', 10) in my_dictionary.items():
    print("Item ('duration', 10) Found")


print("#"*40, end="\n\n")
############################