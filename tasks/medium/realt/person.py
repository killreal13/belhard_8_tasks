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
            print('Надо было в БИП поступать..')
