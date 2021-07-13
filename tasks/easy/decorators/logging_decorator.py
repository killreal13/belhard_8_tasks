"""
Написать логгирующий декоратор, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def method_dec(method):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {method.__name__} с args: {args} и kwargs {kwargs}')
        method(*args, **kwargs)
        print(f'Выполнено {method.__name__}')
    return wrapper


def class_decorator(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for name, value in methods.items():
        method_name = str(value.__name__)
        if method_name.startswith('__'):
            continue
        else:
            dec_method = method_dec(value)
            setattr(cls, name, dec_method)
    return cls


@class_decorator
class Nations:
    skin_color: str
    people_amount: int
    average_iq: int

    def __init__(self, skin_color, people_amount, average_iq):
        self.skin_color = skin_color
        self.people_amount = people_amount
        self.average_iq = average_iq

    def people_reproduction(self):
        if self.skin_color == "yellow":
            self.people_amount += self.people_amount
            return self.people_amount
        else:
            self.people_amount += self.people_amount * 0.5
            return self.people_amount

    def self_improve(self):
        self.average_iq += 10

    def genocide(self):
        self.people_amount = 0
        return self.people_amount

    def __eq__(self, other):
        return self.average_iq == other.average_iq

    def __lt__(self, other):
        return self.average_iq < other.average_iq


asian = Nations('white', 1233, 200)
asian.self_improve()