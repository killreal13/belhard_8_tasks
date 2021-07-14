from tomato import Tomato
from tomato_bush import TomatoBush


class Gardener:
    name: str
    plants: list = []

    def __init__(self, name, *args: TomatoBush):
        self.name = name
        for q in range(len(args)):
            self.plants.append(args[q])

    def work(self):
        for i in self.plants:
            TomatoBush.grow_all(i)

    def harvest(self):
        counter = 0
        for i in self.plants:
            if TomatoBush.all_are_ripe(i):
                counter += 1
            if counter == len(self.plants):
                TomatoBush.give_away_all(i)
        if counter != len(self.plants):
            print('fuck u')


to_1 = Tomato(1)
to_2 = Tomato(2)
to_3 = Tomato(3)
to_4 = Tomato(4)
to_5 = Tomato(5)
to_6 = Tomato(6)
bush = TomatoBush(to_1, to_2, to_3)
bush_2 = TomatoBush(to_2, to_3, to_4)
gardener_vova = Gardener('VOVA', bush, bush_2)
gardener_vova.work()
gardener_vova.work()
gardener_vova.work()
print(gardener_vova.harvest())



