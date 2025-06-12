import random

from faker import Faker
faker = Faker(locale="fr_FR")

class Login:

    @staticmethod
    def email_create_account():
        return {
            "email": faker.email()
        }

    @staticmethod
    def form_create_account():
        return {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "password": faker.password(),
            "dayBirth": str(random.randint(1, 28)),
            "monthBirth": str(random.randint(1, 13)),
            "yearBirth": faker.year()
        }