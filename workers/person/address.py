
class Address:

    def __init__(self, country, city):
        self.check(country, city)
        self.country = country
        self.city = city
        self.address = self.address()

    def __str__(self):
        return " country: " + str(self.country) + " city: " + str(self.city)

    def address(self):  # instance method
        return "%s %s %s" % (self.country, self.city, self._other_details())

    def _other_details(self):
        raise NotImplementedError("To be implemented")

    def check(self, country, city):
        self.check_empty(country, "country")
        self.check_empty(city, "city")

    @staticmethod
    def check_empty(val, name):
        if not val:
            raise ValueError(name + " cannot be empty\n")


class StreetAddress(Address):
    def __init__(self, country, city, street_name, house_number):
        self.street_name = street_name
        self.house_number = house_number
        super().__init__(country, city)

    def __str__(self):
        return super().__str__() + " street name: " + str(self.street_name) + " house number: " + self.house_number

    def _other_details(self):
        return "%s %s" % (self.street_name, self.street_name)


class PobAddress(Address):
    def __init__(self, country, city, pob_number):
        self.pob_number = pob_number
        super().__init__(country, city)

    def __str__(self):
        return super().__str__() + " pob number: " + str(self.pob_number)

    def _other_details(self):
        return "%s" % self.pob_number

"""
for x in range(3):
    a = PobAddress("hjg", "jhfkjd", 8888)
    print(str(a))
"""