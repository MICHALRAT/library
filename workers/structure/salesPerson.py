from workers.structure.worker import Worker


class SalesPerson(Worker):
    def __init__(self, first_name, last_name, year_of_birth, email, address, phones, salary, commission, deals=[]):
        super().__init__(first_name, last_name, year_of_birth, email, address, phones, salary)
        self.commission = commission
        self.deals = deals

    def get_salary(self):
        return super(SalesPerson, self).get_salary()+int(self.commission)*sum(int(self.deals))
