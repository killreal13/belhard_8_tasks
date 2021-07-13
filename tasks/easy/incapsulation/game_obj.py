"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- x int
- y int

Координаты должны быть доступны для чтения, а их изменение должно происходить в методе
move(delta_x, delta_y)

реализовать через property
"""


class GameObject:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = delta_x
        self.y = delta_y


    @property
    def delta_x(self):
        return self.x

    @delta_x.setter
    def delta_x(self, delta_x):
        self.x = delta_x

    @property
    def delta_y(self):
        return self.y

    @delta_y.setter
    def delta_y(self, delta_y):
        self.y = delta_y