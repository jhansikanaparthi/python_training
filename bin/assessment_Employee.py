def my_company_decorator(func):
    def wrapper(self):
        print("Company Name Is: \"XYZ Company\"")
        func(self)
        print("Address: XYZ Address")
    return wrapper

class EmployeeClass:
    company_head_name = None

    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.emp_name):
            char = self.emp_name[self._index]
            self._index += 1
            return char
        else:
            raise StopIteration

    def display_details(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: {self.emp_salary}")
    
    @my_company_decorator
    def get_emp_name(self):
        print(self.emp_name)
    
    @my_company_decorator
    def get_emp_id(self):
        print(self.emp_id)
    
    @my_company_decorator
    def get_emp_salary(self):
        print(self.emp_salary)
    
    @classmethod
    def set_company_head_name(cls, name):
        cls.company_head_name = name
    
    @classmethod
    def get_company_head_name(cls):
        return cls.company_head_name
    
    @staticmethod
    def compute_avg_salary(*salaries):
        if len(salaries) < 2:
            raise ValueError("At least two salaries must be provided to compute the average.")
        return sum(salaries) / len(salaries)

# Example Usage
e1 = EmployeeClass('emp-1', 100, 1000)
e1.display_details()
e1.get_emp_name()
e1.get_emp_id()
e1.get_emp_salary()

for c in e1:
    print("Each Char:", c)

EmployeeClass.set_company_head_name('head-1')
print(EmployeeClass.get_company_head_name())

# Compute Average Salary
print(EmployeeClass.compute_avg_salary(1000, 2000, 3000))
