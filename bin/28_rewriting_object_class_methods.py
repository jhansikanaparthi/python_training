"""
Rewriting methods which is coming from 'object' class

2 methods
Constructor: __new__ which has logic to construct the object
Initializer: __init__
When we create object, both methods will execute

Here 2 cases
Case-1: Overriding __init__ method to store employee name
Case-2: Declaring variables inside class
"""

print("Case-1: Overriding __init__ method to store employee name")
print("-"*20)
# -------------


class Employee:

    # 1. add method to store employee name
    def __init__(self, en):
        self.name = en

    # 2. add method to get employee name
    def get_employee_name(self):
        return self.name

    company_name = "XYZ Company"

    # 4. add method to get company name
    @classmethod
    def get_company_name(cls):
        return cls.company_name

    # 5. add method employee_name_startswith
    def employee_name_startswith(self, prefix):
        employee_name = self.name
        # OR
        employee_name = self.get_employee_name()
        if employee_name.startswith(prefix):
            return True
        else:
            return False

    # 6. add method to compute average salary
    @staticmethod
    def compute_average_salary(s1, s2):
        return (s1+s2)/2

print("#"*40, end="\n\n")
############################

print("Creating 2 objects")
print("-"*20)
# -------------

e1 = Employee("emp-1")
e2 = Employee("emp-2")

print("#"*40, end="\n\n")
############################

print("Total we have 3 objects")
print("-"*20)
# -------------

# CLASS OBJECT: 'Employee': In the name of class,
#           one object will get created automatically
# INSTANCE OBJECTS: e1 & e2 which we are creating


print("#"*40, end="\n\n")
############################

print("DATA present in each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee.get_company_name())
print("DATA present in instance object 'e1':", e1.get_employee_name())
print("DATA present in instance object 'e2':", e2.get_employee_name())

print("#"*40, end="\n\n")
############################

print("METHODS/VARIABLES present in each objects")
print("-"*20)
# -------------

print("METHODS/VARIABLES present in class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################