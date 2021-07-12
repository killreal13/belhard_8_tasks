"""
Описать класс Transport, у которого следующие атрибуты:

- brand - фирма, выпустившая транспорт
- model - модель
- issue_year - год выпуска
- color - цвет

Определить методы:

- move - который делает raise NotImplementedError

Описать класс Car, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- engine_type

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} проехала {km} километров"

Описать класс Airplane, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- lifting_capacity - грузоподъемность

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} пролетел {km} километров"
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    brand: str
    model: str
    issue_year: int
    color: str

    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    @abstractmethod
    def move(self):
        raise NotImplementedError


class Car(Transport):
    mileage: int
    engine_type: str

    def __init__(self, brand, model, issue_year, color, mileage, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.mileage = mileage
        self.engine_type = engine_type

    def move(self, km):
        self.mileage += km
        print(f'{self.brand} {self.model} проехала {km} километров')


class Airplane(Transport):
    mileage: int
    lifting_capacity: int

    def __init__(self, brand, model, issue_year, color, mileage, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.mileage = mileage
        self.lifting_capacity = lifting_capacity

    def move(self, km):
        self.mileage += km
        print(f'{self.brand} {self.model} пролетел {km} километров')
