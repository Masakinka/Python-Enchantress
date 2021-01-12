"""
This is a class Person.
"""
from abc import ABC, abstractmethod
import datetime
import random


# class of Human
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
        self.cost = self.area * 3348

    def get_parameters(self):
        return self.cost

    def info(self):
        print(f'From area {self.area} m2. House cost is {self.cost} $.')


class Person(Human):
    def __init__(self, name, birthday, home, money, cost):
        self.name = name
        self.birthday = birthday
        self.money = money
        self.home = home
        self.cost = cost

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year

        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1
        return age

    def about_yourself(self):
        print(f'Hi! I am {self.name}. My age is {self.calculate_age()}.')
        if self.home == 0:
            print(f'I haven`t a home.')
        else:
            print(f'I have a {self.home} home!.')
        if self.money == 0:
            print(f'I haven`t a money.')
        else:
            print(f'I have a {self.money} money $.')

    def make_money(self):
        if self.calculate_age() > 18:
            self.money += 5000
            print(f'Work...Work...)')
            print(f'I have a {self.money} $.')
        else:
            print(f'You are too young. You are only {self.calculate_age()} years old.')

    def buy_house(self):
        if self.money >= self.cost:
            self.money -= self.cost
            self.home += 1
            print(f'Congratulations, {self.name}! You bought a house!')
        else:
            print(f'Sorry, {self.name}, you haven`t enough money to buy this house.')

    def make_purchase(self, discount=0.1):
        if self.money < self.cost:
            amount = self.cost - self.cost * discount
            print(f' {self.name}, you used {discount}%. New prise is {amount}$')
        else:
            print(f'Sorry, {self.name}, you have enough money to buy this house')


if __name__ == "__main__":
    home_parameter1 = House(random.randint(20, 180))
    home_parameter2 = House(random.randint(20, 180))
    home_parameter3 = House(random.randint(20, 180))

    homes = [home_parameter1, home_parameter2, home_parameter3]
    for home_parameter in homes:
        home_parameter.info()

    person1 = Person("Vi", datetime.date(1991, 5, 24), 0, random.randint(0, 20000000), home_parameter1.get_parameters())
    person2 = Person("Ka", datetime.date(2018, 5, 24), 0, 0, home_parameter2.get_parameters())
    person3 = Person("Vo", datetime.date(1993, 4, 22), 0, random.randint(0, 10000), home_parameter3.get_parameters())
    persons = [person1, person2, person3]
    for person in persons:
        person.about_yourself()
        person.make_money()
        person.buy_house()
        person.make_purchase()
