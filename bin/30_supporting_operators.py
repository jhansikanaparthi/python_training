"""
Here 2 things:
1. Support + operator
2. Make it iterable

In python, for each opeator there is name given,
example: for + name is __add__

So, if we want to support for + then we need  to write __add__ method
inside that class
"""
print("Supporting + operator")
print("-"*20)
# -------------

class Employee:
    def __init__(self, en):
        self.name = en

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result

    def __sub__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result

e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Requirement: if we add, both names should concat
add_result = e1 + e2 # e1.__add__(e2) # 'emp-1emp-2'
print("add_result:", add_result)

add_result = e1 - e2 # e1.__add__(e2) # 'emp-1emp-2'
print("add_result:", add_result)

print("#"*40, end="\n\n")
############################
print("Supporting Iteration")
print("-"*20)
# -------------

class Employee:
    def __init__(self, en):
        self.name = en

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result

    def __iter__(self):
        self.index_no = 0
        return self

    def __next__(self):
        current_index = self.index_no
        if current_index < len(self.name):
            self.index_no = self.index_no + 1
            return self.name[current_index]
        else:
            raise StopIteration


e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Requirement: if we add, both names should concat
add_result = e1 + e2 # e1.__add__(e2) # 'emp-1emp-2'
print("add_result:", add_result)

print("Iterating e1:", e1.name, end="\n\n")
for i in e1:
    print("Each char:", i)

print("\n")

print("Iterating e2:", e2.name, end="\n\n")
for i in e2:
    print("Each char:", i)

print("\n")

print("#"*40, end="\n\n")
############################