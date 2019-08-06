from workers.structure.worker import Worker


class Engineer(Worker):
    def __init__(self, first_name, last_name, year_of_birth, email, address, phones, salary, bonus):
        super().__init__(first_name, last_name, year_of_birth, email, address, phones, salary)
        self.bonus = bonus

    def get_salary(self):
        return super(Engineer, self).get_salary()+int(self.bonus)
