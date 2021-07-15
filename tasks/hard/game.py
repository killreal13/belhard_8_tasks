"""
Создать класс Warrior

Определить атрибуты:

- name - имя юнита
- health_points - int от 0 до 100

Определить методы:

- инициализатор __init__, который создает юнита со 100 health_points
- метод hit, который реализует удар, от которого снимается 20 health_points
  у другого юнита

Создать список, в который добавить 5 объектов класса Warrior.

В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение, какой юнит атаковал,
и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья он удаляется из списка.
Программа завершается, когда останется один юнит, на экран выводится сообщение о том,
кто одержал победу.
"""
import random


class Warrior:
    name: str
    health_points: int

    def __init__(self, name):
        self.name = name
        self.health_points = 100

    def hit(self, other_warrior):
        other_warrior.health_points -= 20
        print(f'{self.name} attacked {other_warrior.name} and left him {other_warrior.health_points} health points')


class Arena:
    warrior_list: list

    def __init__(self, warriors_list):
        self.warrior_list = warriors_list

    def fight(self):
        while True:
            for i in range(len(self.warrior_list)):
                attacking_warrior = random.choice(self.warrior_list)
                defending_warrior = random.choice(self.warrior_list)
                if attacking_warrior.name == defending_warrior.name:
                    continue
                else:
                    Warrior.hit(attacking_warrior, defending_warrior)
                if defending_warrior.health_points == 0:
                    self.warrior_list.remove(defending_warrior)
            if len(self.warrior_list) == 1:
                print(f'{self.warrior_list[0].name} wins!')
                break


warrior_1 = Warrior('Deiveson Figueiredo')
warrior_2 = Warrior('Dustin Poirier')
warrior_3 = Warrior('Edson Barboza')
warrior_4 = Warrior('Charles Oliveira')
warrior_5 = Warrior('Max Holloway')

warrior_list = [warrior_1, warrior_2, warrior_3, warrior_4, warrior_5]
arena_1 = Arena(warrior_list)
arena_1.fight()
