"""
Создать 3 класса:

Cat, Duck, Cow

в каждом классе определить метод says()

Cat.says() - кошка говорит мяу
Duck.says() - утка говорит кря
Cow.says() - корова говорит муу


Написать функцию animal_says(), которая принимает объект и вызывает метод says
"""


class Cat:

    def says(self):
        print("Cat says Meow")


class Duck:

    def says(self):
        print("Duck says Crya")


class Cow:

    def says(self):
        print("Cow says Moo")


def animal_says(object_name):
    object_name.says()


cat_1 = Cat()
duck_1 = Duck()
cow_1 = Cow()
