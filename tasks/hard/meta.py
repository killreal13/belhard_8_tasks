"""
Создать метакласс, который будет фиксировать тип атрибута с помощью аннотаций.
При попытке присвоить атрибуту объект не подходящего типа сгенерировать исключение
ValueError
"""


def attribute_checker(method):
    def wrapper(self, name, values):
        attribute_annotation = self.__annotations__.get(name)
        if type(values) != attribute_annotation:
            raise ValueError
        return method(self, name, values)
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

aasd = Strings('123', 123)
print(aasd.values)