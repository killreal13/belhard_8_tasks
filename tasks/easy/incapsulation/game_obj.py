"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- x int
- y int

Координаты должны быть доступны для чтения, а их изменение должно происходить в методе
move(delta_x, delta_y)

реализовать через property
"""


class GameObject:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def delta_x(self):
        return self.__x

    @property
    def delta_y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x += delta_x
        self.__y += delta_y

