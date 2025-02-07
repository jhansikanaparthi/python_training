"""
Inheritance:
1. multilevel inheritance
2. multiple inheritance
"""

print("1. multilevel inheritance")
print("-"*20)
# -------------


# Assume below class is existing class
class Salary:
    def add_salary(self, sal):
        self.salary = sal

    def get_salary(self):
        return self.salary

# Client New Requirement
# 1. add_tax method
# 2. get_tax method
# 3. modify get_salary method to return (salary-tax)
# 4. add method to get old_salary

# Employee -> subclass/child-class
# Salary -> superclass/parent class
class Employee(Salary):
    # 1. add_tax method
    def add_tax(self, t):
        self.tax = t

    # 2. get_tax method
    def get_tax(self):
        return self.tax

    # 3. modify get_salary method to return (salary-tax)
    # POLYMORPHISM: WE can reuse same name as super class method
    def get_salary(self): # This will OVERRID super class get_salary
        return self.salary - self.tax

    # 4. add method to get old_salary
    def get_old_salary(self):
        old_salary = super().get_salary()
        # OR
        old_salary = Employee.get_salary(self)
        return old_salary

e1 = Employee()
e1.add_salary(20000)
e1.add_tax(200)

print("Salary:", e1.get_salary())
print("OLD Salary:", e1.get_old_salary())
print("Tax:", e1.get_tax())

print("#"*40, end="\n\n")
##########################
print("1. multilevel inheritance: Method RESOLUTION order")
print("-"*20)
# -------------

print(Employee.mro())

print("#"*40, end="\n\n")
############################

print("2. multiple inheritance: Method RESOLUTION order")
print("-"*20)
# -------------

class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(C.mro())

print("#"*40, end="\n\n")
############################