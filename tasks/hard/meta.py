"""
Создать метакласс, который будет фиксировать тип атрибута с помощью аннотаций.
При попытке присвоить атрибуту объект не подходящего типа сгенерировать исключение
ValueError
"""


def attribute_checker(method):
    def wrapper(*args, **kwargs):
        if method.__name__ == '__setattr__':
            if
        method(*args, **kwargs)
    return wrapper


class AttributeTypeMeta(type):
    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)
        attr_dict = {k: v for k, v in mcs.__dict__.items() if callable(v)}
        for k, v in attr_dict.items():
            new_value = attribute_checker(v)
            setattr(new_class, k, new_value)
        return new_class


class Strings(metaclass=AttributeTypeMeta):
    values: str
    qwe: int

    def __init__(self, values, qwe):
        self.values = values
        self.qwe = qwe

    def print_values(self, a):
        print(self.values, a)

aasd = Strings('44', 123)
aasd.print_values(12)