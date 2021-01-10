"""
This is a class Person.
"""
from abc import ABC, abstractmethod
import datetime
import random


# classes of Human
class Human(ABC):

    @abstractmethod
    def about_yourself(self):
        raise NotImplementedError('You need to add information message in future.')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('You need to add function which can make money in future.')

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError('You need to add function which can buy house in future.')


class House:
    def __init__(self, area):
        self.area = area
        self.cost = self.area * 33483

    def info(self):
        print(f'From area {self.area} m2. House cost is {self.cost} $.')


class Person(Human):
    def __init__(self, name, birthday, home, money):
        self.name = name
        self.birthday = birthday
        self.money = money
        self.home = home

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year

        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1
        return age

    def about_yourself(self):
        print(f'Hi! I am {self.name}. My age is {self.calculate_age()}.')
        if not self.home:
            print(f'I haven`t a home.')
        else:
            print(f'I haven`t a home! {self.home}.')
        if not self.money:
            print(f'I haven`t a money.')
        else:
            print(f'I have a {self.money} money.')

    def make_money(self):
        if self.calculate_age() > 18:
            self.money += 5000
            print(f'Work...Work...)')
            print(f'I have a {self.money} $.')
        else:
            print(f'You are too young. You are only {self.calculate_age()} years old.')


    def buy_house(self):
        if self.money == House.cost:
            self.money -= House.cost
            self.home = 1
            print(f'Congratulations, {self.name}! You bought a house! With {House.area}')
        else:
            print(f'Sorry, {self.name}, you haven`t enough money to buy this house)')

    def make_purchase(self):
        discount = 0.1
        amount = House.cost - House.cost * discount
        print(f' {self.name}, you used {discount}% . New prise is {amount}')


if __name__ == "__main__":
    person = Person("Vi", datetime.date(1991, 5, 24), 0, 0)
    home = House(random.randint(20, 180))
    # home = House(10)
    home.info()
    person.about_yourself()
    person.make_money()
    person.buy_house()
    person.make_purchase()
    # person.calculate_age()
