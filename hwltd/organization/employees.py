class Employees:
    def __init__(self, employees={}):
        self.employees = employees

    def add_employee(self, name, email):
        self.employees[email] = name

"""
e = Employees()
e.add_employee("msms","fdfds")
print(e.employees)
"""