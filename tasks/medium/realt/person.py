from house import House
from townhouse import Townhouse


class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(self.name, self.age, self.money, self.realty)

    def earn_money(self, increase_value):
        self.money += increase_value

    def make_deal(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.realty.append(house)
        else:
            print('Квартиру себе купи и живи отдельно..')


new_house = Townhouse('55 st', 100000)
new_person = Person('killreal', 21)
new_person.earn_money(200000)
new_person.make_deal(new_house)
print(new_person.realty)