"""
- Frozenset:
        -- We have option to store multiple values like list names etc
        -- Here, we can store UNIQUE values
        -- No index will be assigned to each value
"""

print("Frozenset PART-1")
print("Store the values")
print("-"*20)
# -------------

my_fs = frozenset([10, 10, 10, "python", "python", "python", "java", "java"])
print(my_fs)

# Convert to other type if we want index number
# OR
# We can also iterate for-loop/while-loop
my_tuple = tuple(my_fs)
my_list = list(my_fs)

print("#"*40, end="\n\n")
############################

print("Frozenset PART-2")
print("METHODS present in 'frozenset' class")
print("-"*20)
# -------------

print(dir(my_fs))
# OR
# print(dir(frozenset))

print("#"*40, end="\n\n")
############################

print("Frozenset PART-3")
print("union, intersection, difference methods")
print("-"*20)
# -------------

batch_1_condidates = frozenset(["emp-1", "emp-2", "emp-3", "emp-4"])
batch_2_condidates = frozenset(["emp-3", "emp-4", "emp-5", "emp-6"])

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