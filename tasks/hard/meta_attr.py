"""
Предположим, нас утомило задание атрибутов в конструкторе init(self, *args,
**kwargs). Хотелось бы ускорить этот процесс таким образом, чтобы была
возможность задавать атрибуты прямо при создании объекта класса.

class Man(object):
    pass

me = Man(height = 180, weight = 80)
Traceback (most recent call last):
File "<stdin>", line 20, in <module>
    TypeError: object.new() takes no parameters

Сделать возможным данный механизм
"""
def getattr_1(method):
    def wrapper(self, name, value):
        print(name)
    return wrapper



class AttributeMeta(type):
    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)
        new_class.__setattr__ = getattr_1(new_class.__setattr__)
        print(new_class.__setattr__)
        return new_class


class Man(metaclass=AttributeMeta):
    pass

me = Man(qwe = 80, qr = 100)
