from workers.person.person import Person


class Worker:
    def __init__(self, first_name, last_name, year_of_birth, email, address, phones, salary):
        self.salary = salary
        self.person = Person(first_name, last_name, year_of_birth, email, address, phones)

    def get_salary(self):
        return int(self.salary)
