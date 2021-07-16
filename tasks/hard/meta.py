"""
Создать метакласс, который будет фиксировать тип атрибута с помощью аннотаций.
При попытке присвоить атрибуту объект не подходящего типа сгенерировать исключение
ValueError
"""


def attribute_checker(method):
    def wrapper(self, name, value):
        attribute_annotation = self.__annotations__.get(name)
        if type(value) != attribute_annotation and attribute_annotation is not None:
            raise ValueError
        return method(self, name, value)
    return wrapper


class AttributeTypeMeta(type):

    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)
        new_class.__setattr__ = attribute_checker(new_class.__setattr__)
        return new_class


class Strings(metaclass=AttributeTypeMeta):
    values: str
    qwe: int

    def __init__(self, values, qwe):
        self.values = values
        self.qwe = qwe

    def print_values(self, a):
        print(self.values, a)


strings_1 = Strings('123', 123)
print(strings_1.values)
