"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    a_type: user should enter type of animal(wild or homing)
    """
    name: str
    a_type: str

    def __init__(self, name, a_type):
        self.name = name
        self.a_type = a_type

    @abstractmethod
    def says(self):
        pass


class Cat(Animal):

    def __init__(self, name, a_type):
        super().__init__(name, a_type)

    def says(self):
        print(f"Cat {self.name} says МEOW")


class Dog(Animal):

    def __init__(self, name, a_type):
        super().__init__(name, a_type)

    def says(self):
        print(f"Dog {self.name} says BARK")


class Cow(Animal):

    def __init__(self, name, a_type):
        super().__init__(name, a_type)

    def says(self):
        print(f"Cow {self.name} says МOO")
