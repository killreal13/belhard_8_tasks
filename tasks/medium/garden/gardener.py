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
        all_tomatoes = []
        counter = 0
        for i in self.plants:
            if TomatoBush.all_are_ripe(i):
                counter += 1
            if counter == len(self.plants):
                all_tomatoes.append(TomatoBush.give_away_all(i))
        if counter != len(self.plants):
            print('Томаты не созрели')
            return None
        else:
            return all_tomatoes[0]




