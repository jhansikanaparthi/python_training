"""
How to add methods?

Requirement:
1. add method to store employee name
2. add method to get employee name
3. add method to store company name
4. add method to get company name
5. add method employee_name_startswith
6. add method to compute average salary
"""
print("Creating new class")
print("-"*20)
# -------------


class Employee:
    """
    Requirement:
        1. add method to store employee name
        2. add method to get employee name
        3. add method to store company name
        4. add method to get company name
        5. add method employee_name_startswith
        6. add method to compute average salary
    """
    # 1. add method to store employee name
    def store_employee_name(self, en):
        self.name = en

    # 2. add method to get employee name
    def get_employee_name(self):
        return self.name

    # 3. add method to store company name
    @classmethod
    def store_company_name(cls, cn):
        cls.company_name = cn

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

e1 = Employee()
e2 = Employee()

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

print("Store Data Inside Objects")
print("-"*20)
# -------------

# Store in Employee object
# -------------
Employee.store_company_name("XYZ Company")
# Internally object 'Employee' will be passed to 'cls'

e1.store_company_name("XYZ Company")
# Internally object 'e1' WILL NOT BE PASSED TO 'cls'
# @classmethod will take care of passing class object only to 'cls'
###############

# Store in Employee name
# -------------
e1.store_employee_name("emp-1")
# Internally 'e1' will be passed to 'self'
# OR
Employee.store_employee_name(e2, "emp-2")
###############


# Store in Employee name
# -------------
e2.store_employee_name("emp-2")
# Internally 'e2' will be passed to 'self'
# OR
Employee.store_employee_name(e2, "emp-2")
###############

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

print("Other Methods")
print("-"*20)
# -------------

starts_with_result = e1.employee_name_startswith("emp")
print("starts_with_result:", starts_with_result)

s1 = 1000
s2 = 2000
avg_salary = e1.compute_average_salary(s1, s2)
print("avg_salary:")

print("#"*40, end="\n\n")
############################