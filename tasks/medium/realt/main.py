from house import House
from townhouse import Townhouse
from person import Person


if __name__ == '__main__':
    house_1 = House('Abbey Road', 32, 50000)
    house_2 = House('Piccadilly', 47, 87000)
    house_3 = Townhouse('Princess St', 120000)
    house_4 = Townhouse('Baker St', 98500)
    person_1 = Person('killreal', 13)
    person_1.make_deal(house_4)
    person_1.earn_money(36000)
    person_1.make_deal(house_4)
    person_1.earn_money(100000) #получил наследство от бабушки из Бастилии
    person_1.make_deal(house_4)
    person_1.earn_money(500000) #выиграл в казино
    person_1.make_deal(house_1) #процесс становления хозяином жизни
    person_1.make_deal(house_3)
    person_1.make_deal(house_2) #стал хозяином жизни