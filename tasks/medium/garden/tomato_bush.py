from tomato import Tomato


class TomatoBush:
    tomato_list: list

    def __init__(self, *args: Tomato):
        self.tomato_list = args

    def grow_all(self):
        for i in self.tomato_list:
            Tomato.grow(i)

    def all_are_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False

    def give_away_all(self):
        tomato_list_2 = self.tomato_list
        self.tomato_list = list(self.tomato_list).clear()
        return list(tomato_list_2)

to_1 = Tomato(1)
to_2 = Tomato(2)
to_3 = Tomato(3)
bush = TomatoBush(to_1, to_2, to_3)
print(bush.tomato_list)
bush.grow_all()
print(to_2.ripeness)


