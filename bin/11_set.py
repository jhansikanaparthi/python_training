"""
- set:
        -- We have option to store multiple values like list names etc
        -- Here, we can store UNIQUE values
        -- No index will be assigned to each value
"""

print("set PART-1")
print("Store the values")
print("-"*20)
# -------------

my_set = {10, 10, 10, "python", "python", "python", "java", "java"}
print(my_set)

my_set = set([10, 10, 10, "python", "python", "python", "java", "java"])
print(my_set)

# Convert to other type if we want index number
# OR
# We can also iterate for-loop/while-loop
my_tuple = tuple(my_set)
my_list = list(my_set)

print("#"*40, end="\n\n")
############################

print("set PART-2")
print("METHODS present in 'set' class")
print("-"*20)
# -------------

print(dir(my_set))
# OR
# print(dir(set))

print("#"*40, end="\n\n")
############################

print("set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# -------------

batch_1_condidates = set(["emp-1", "emp-2", "emp-3", "emp-4"])
batch_2_condidates = set(["emp-3", "emp-4", "emp-5", "emp-6"])

print("batch_1_condidates:", batch_1_condidates)
print("batch_2_condidates:", batch_2_condidates, end="\n\n")

all_condidates = batch_1_condidates.union(batch_2_condidates)
print("all_condidates:", all_condidates)

candidates_present_in_both = batch_1_condidates.intersection(batch_2_condidates)
print("candidates_present_in_both:", candidates_present_in_both)

candidates_present_in_only_batch_1 = batch_1_condidates.difference(batch_2_condidates)
print("candidates_present_in_only_batch_1:", candidates_present_in_only_batch_1)

print("#"*40, end="\n\n")
############################

print("set PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -------------

batch_1_condidates = {"emp-1", "emp-2", "emp-3", "emp-4"}
print("batch_1_condidates:", batch_1_condidates, end="\n\n")

# ADD
batch_1_condidates.add("emp-5")
print("batch_1_condidates after adding emp-5:", batch_1_condidates, end="\n\n")
# {"emp-1", "emp-2", "emp-3", "emp-4", emp-5}

# REMOVE
batch_1_condidates.remove("emp-1")
print("batch_1_condidates after removing emp-1:", batch_1_condidates, end="\n\n")
# {"emp-2", "emp-3", "emp-4", emp-5}

# UPDATE
another_set = {"emp-6", "emp-7"}
print("another_set:", another_set)
batch_1_condidates.update(another_set)
print("batch_1_condidates after updating another set:", batch_1_condidates, end="\n\n")

# How to update "emp-6" with "emp-8"
batch_1_condidates.remove("emp-6")
batch_1_condidates.add("emp-8")
print("batch_1_condidates after updating 'emp-6' with 'emp-8':", batch_1_condidates, end="\n\n")

print("#"*40, end="\n\n")
############################