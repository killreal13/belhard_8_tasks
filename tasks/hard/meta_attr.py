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


class AttributeMeta(type):
    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)
        new_attrs = {k: v for k, v in bases.items()}
        for k, v in new_attrs.items():
            setattr(new_class, k, v)
        return new_class





class me = Man(height = 180, weight = 80)
