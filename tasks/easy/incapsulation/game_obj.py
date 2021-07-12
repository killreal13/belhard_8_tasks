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

    @property
    def move(self):
        return self.x, self.y

    @move.setter
    def move(self, x, y):
        self.x = x
        self.y = y
