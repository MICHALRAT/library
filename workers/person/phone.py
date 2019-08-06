import re


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return str(self._phone_number)

    @property
    def phone_number(self):
        self._phone_number

    @phone_number.setter
    def phone_number(self, em):
        if not em:
            raise ValueError("email cannot be empty\n")
        match = re.match('^([+]*)+([0-9-]+)', em)
        if match is None:
            raise ValueError('Bad Syntax for phone number\n')
        self._phone_number = em


"""try:
    PhonesString = input("\nEnter Phones: \n")
    p = Phone(PhonesString)
    print(p)
except ValueError as e:
    print(e)
"""
