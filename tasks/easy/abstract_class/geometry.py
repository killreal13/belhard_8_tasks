"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    pi = 3.14

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    radius: float

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * Shape.pi * self.radius

    def get_square(self):
        return Shape.pi * self.radius ** 2


class Rectangle(Shape):
    first_side_length: float
    second_side_length: float

    def __init__(self, first_side_length, second_side_length):
        self.first_side_length = first_side_length
        self.second_side_length = second_side_length

    def get_perimeter(self):
        return 2 * self.first_side_length + 2 * self.second_side_length

    def get_square(self):
        return self.first_side_length * self.second_side_length


class Square(Rectangle):

    def __init__(self, first_side_length, second_side_length):
        super().__init__(first_side_length, second_side_length)

    def get_perimeter(self):
        return 4 * self.first_side_length

    def get_square(self):
        return self.first_side_length ** 2
