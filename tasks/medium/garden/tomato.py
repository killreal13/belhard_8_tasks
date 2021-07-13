class Tomato:
    index: int
    ripeness: str
    states: tuple = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        current_stage = self.states.index(self.ripeness)
        self.ripeness = self.states[current_stage + 1]

    def is_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False

