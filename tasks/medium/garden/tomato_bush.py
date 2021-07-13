from tomato import Tomato


class TomatoBush(Tomato):
    tomato_list: list = []

    def __init__(self, *args):
        self.tomato_list = args
        self.ripeness = self.states[0]

    def grow_all(self):
        current_stage = self.states.index(self.ripeness)
        self.ripeness = self.states[current_stage + 1]

    def all_are_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False

    def give_away_all(self):
        tomato_list_2 = self.tomato_list
        self.tomato_list = list(self.tomato_list).clear()
        return list(tomato_list_2)

asd = TomatoBush(1, 2, 3)
print(asd.tomato_list)
print(asd.grow_all())
print(asd.ripeness)
asd.give_away_all()