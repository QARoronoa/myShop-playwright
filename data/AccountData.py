from faker import Faker

faker = Faker(locale= "fr_FR")
class Account:

    @staticmethod
    def fill_address_form():
        return {
            "address": faker.address(),
            "city": faker.city(),
            "zipCode": "23232",
            "homePhone": faker.phone_number(),
            "mobilePhone": faker.phone_number(),
            "addressTitle" : faker.name()
        }