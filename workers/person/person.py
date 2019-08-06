import re
from workers.person.phone import Phone
from workers.person.address import PobAddress
from workers.person.address import StreetAddress


class Person:
    id = 0

    def __init__(self, first_name, last_name, year_of_birth, email, address, phones):
        """the init function to initialize the person object"""
        self.check(first_name, last_name, email)
        self._first_name = first_name
        self._last_name = last_name
        self._year_of_birth = year_of_birth
        self._email = email
        self.phones = []
        self.add_phones(phones)
        self.address = self.add_address(address)
        self.id_increment()

    def __str__(self):
        """method that sends person type to be printed"""
        phone_str = " "
        for y in self.phones:
            phone_str += str(y) + " "
        return "\nid: " + str(self.id) + "\n first name: " + str(self._first_name) + "\n last name: " \
               + str(self._last_name) + "\n email: " + str(self._email) + "\n year of birth: " + \
               str(self.year_of_birth) + "\n address: " + str(self.address) + "\n phones: " + str(phone_str)

    def check(self, first_name, last_name, email):
        self.check_empty(first_name, "first name")
        self.check_empty(last_name, "last name")
        self.check_empty(email, "email")
        self.check_email(email)

    def check_email(self, email):
        if self.email_reg(email) is None:
            raise ValueError('Bad Syntax for email address: ' + email + "\n")

    @staticmethod
    def check_empty(val, name):
        if not val:
            raise ValueError(name + " cannot be empty\n")

    @classmethod
    def id_increment(cls):
        cls.id += 1

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, fn):
        raise ValueError("first name cannot be changed")

    @property
    def last_name(self):
        self._last_name

    @last_name.setter
    def last_name(self, ln):
        raise ValueError("last name cannot be changed")

    @property
    def email(self):
        self._email

    @staticmethod
    def email_reg(ema):
        val = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]+)$', ema)
        return val

    @email.setter
    def email(self, em):
        raise ValueError("email cannot be changed")

    @property
    def year_of_birth(self):
        return self._year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, yob):
        if re.match('^[0-9]{4}', yob) is None:
            raise ValueError('Bad Syntax for year of birth\n')

    def add_phones(self, phones):
        for p in phones:
            self.phones.append(Phone(p))

    @staticmethod
    def add_address(address):
        ad = address.split(";")
        # print(ad)
        if len(ad) == 3:
            return PobAddress(ad[0], ad[1], ad[2])
        elif len(ad) == 4:
            return StreetAddress(ad[0], ad[1], ad[2], ad[3])
        raise ValueError("address in wrong format: " + str(ad))

"""
for x in range(2):
    notValid = True
    while notValid:
        try:
            print("\nPlease enter some information\n")
            FirstName = input("\nEnter first name: ")
            LastName = input("\nEnter last name: ")
            Email = input("\nEnter email ")
            YearOfBirth = input("\nyear of birth: ")
            Address = input("\nEnter address: ")
            PhonesString = input("\nEnter Phones: \n")
            Phones = PhonesString.split()
            user = Person(FirstName, LastName, YearOfBirth, Email, Address, Phones)
            print(user)
            user.phones.append("070970")
            print(user)
            notValid = False
        except ValueError as e:
            print(str(e))
            continue
"""