"""
We are keeping
- all variables
- all functions
- all classes
in this file, which we are planning to use in other programs

This file is also called as PYTHON-MODULE or PYTHON-LIBRARY
"""

course = "python"


def add(a, b):
    return a + b


class Employee:
    def store_name(self, en):
        self.name = en
    def get_name(self):
        return self.name