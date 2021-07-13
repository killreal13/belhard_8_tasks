"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.

До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time


def method_dec(method):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {method.__name__} с args: {args} и kwargs: {kwargs}')
        start_time = time.time()
        print(f'Время начала: {start_time}')
        method(*args, **kwargs)
        print(f'Выполнено {method.__name__}')
        end_time = time.time()
        print(f'Время окончания: {end_time}')
        print(f'Время затрачено на выполнение: {end_time - start_time}')
    return wrapper


def class_decorator(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for name, method in methods.items():
        method_name = str(method.__name__)
        if method_name.startswith('__'):
            continue
        else:
            dec_method = method_dec(method)
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
        return self.average_iqiq == other.average_iq

    def __lt__(self, other):
        return self.average_iqiq < other.average_iq


