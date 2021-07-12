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

# start_time = time.time()
# end_time = time.time()
# difference = e - s


def benchmark(cls):
    def wrapper(*args, **kwargs):
        for


@benchmark
class Nations:
    skin_color: str
    people_amount: int
    sex: str
    iq: int

    def __init__(self, skin_color, people_amount, sex, iq):
        self.skin_color = skin_color
        self.people_amount = people_amount
        self.sex = sex
        self.iq = iq

    def __repr__(self):
        return f"{self.skin_color} has {self.iq}"

    def sex_changing(self):
        if self.sex == "male":
            self.sex = "female"
            return self.sex
        elif self.sex == "female":
            self.sex = "male"
            return self.sex
        else:
            print(f"{self.sex} does not exist, there are only two genders!")

    def people_reproduction(self):
        if self.skin_color == "yellow":
            self.people_amount += self.people_amount
            return self.people_amount
        else:
            self.people_amount += self.people_amount * 0.5
            return self.people_amount

    def genocide(self):
        self.people_amount = 0
        return self.people_amount

    def __eq__(self, other):
        return self.iq == other.iq

    def __lt__(self, other):
        return self.iq < other.iq


russian = Nations("white", 12312333, "male", 144)
asian = Nations("yellow", 123123, "female", 222)
qweqwe = Nations("qqqq", 123121233, "female", 15)
asian1 = Nations("yellow", 123123, "female", 2233)

nations = [russian, asian, qweqwe, asian1]
