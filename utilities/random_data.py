from faker import Faker

class RandomData:
    def __init__(self, locale:str = 'en_US'):
        self.__faker:Faker = Faker(locale)

    def first_name(self) -> str:
        return self.__faker.first_name()

    def last_name(self) -> str:
        return self.__faker.last_name()

    def job(self) -> str:
        return self.__faker.job()