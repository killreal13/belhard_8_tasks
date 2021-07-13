"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def logging_dec(method):
    def wrapper(*args, **kwargs):
        print('Выполняем')
        method(*args, **kwargs)
    return wrapper


class LoggingMeta(type):
    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)
        attr_dict = {k: v for k, v in attr.items() if callable(v)}
        for k, v in attr_dict.items():
            method_name = str(v.__name__)
            if method_name.startswith('__'):
                continue
            else:
                new_value = logging_dec(v)
                setattr(new_class, k, new_value)
        return new_class


class Smthg(metaclass=LoggingMeta):
    name: str

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'{self.name}')



