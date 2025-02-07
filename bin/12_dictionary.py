"""
- Dictionary:
        -- We have option to store multiple values like list names etc
        -- Here, we can store DUPLICATE values
        -- Here, MANUALLY we NEED-TO provide index to each value called KEY/VALUE pair.
"""

print("Dictionary PART-1")
print("Store the values")
print("-"*20)
# -------------

my_dictionary_1 = {0:10, 1:"python", 2:"online"}

# FOR KEYS: We can make use of any IMMUTABLE VALUES like numbers, string, tuple
my_dictionary_2 = {"duration":10, "course":"python", "mode":"online"}

# FOR VALUES: We can store any type of values
my_dictionary_3 = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)

print("#"*40, end="\n\n")
############################

print("Dictionary PART-2")
print("Accessing each value using KEY")
print("-"*20)
# -------------
my_dictionary = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n") # 10

print("Course:", my_dictionary["course"]) # python
print("3rd char in Course:", my_dictionary["course"][2], end="\n\n") # 't'

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("Last Mode:", my_dictionary["mode"][-1]) # "offline"
print("4th Char in Last Mode:", my_dictionary["mode"][-1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Last name of the Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd character in Last name of the Trainer:", my_dictionary["trainer"]["lname"][1], end="\n\n") # "y"

print("#"*40, end="\n\n")
############################

print("Dictionary PART-3")
print("List of methods present in 'dict' class")
print("-"*20)
# -------------

print(dir(my_dictionary))
# OR
# print(dir(dict))

print("#"*40, end="\n\n")
############################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE
my_dictionary["location"] = "India"
# If key present UPDATE else add new entry
print("my_dictionary after adding/updating location:", my_dictionary, end="\n\n")
# {"duration":10, "course":"python", "mode":"online", location:India}

another_dictionary = {"trainer":"abc"}
print("another_dictionary:", another_dictionary)
my_dictionary.update(another_dictionary)
print("my_dictionary after adding/updating trainer:", my_dictionary, end="\n\n")
# {"duration":10, "course":"python", "mode":"online", location:India, trainer:abc}

# REMOVE
my_dictionary.pop("duration")
print("my_dictionary after removing duration:", my_dictionary, end="\n\n")
my_dictionary.popitem()
print("my_dictionary after removing last value using popitem():", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
############################
