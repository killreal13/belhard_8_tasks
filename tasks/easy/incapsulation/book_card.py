"""
Создать класс BookCard, в классе должны быть закрытые атрибуты:

- author - автор
- title - название книги
- publishing_house - издательство
- year - год издания
- num_pages - количество страниц
- num_copies - тираж

Определить методы:

- инициализатор __init__
- магические методы сравнения для сортировки книг по году издания

в сеттерах сделать проверки на тип данных. Если тип данных не подходит, то генерировать
ValueError. Для года издания дополнительно проверить на валидность, num_pages и
num_copies должны быть больше 0

реализовать через property
"""


class BookCard:
    _author: str
    _title: str
    _publishing_house: str
    _year: int
    _num_pages: int
    _num_copies: int

    @property
    def __init__(self, author, title, puplishing_house, year, num_pages, num_copies):
        return self._author = author
        return self._title = title
        return self._publishing_house = puplishing_house
        return self._year = year
        return self._num_pages = num_pages
        return self._num_copies = num_copies

    def __eq__(self, other):
        return self._year == other._year

    def __lt__(self, other):
        return self._year < other._year

    @property
    def book(self):
        return self._author, self._title, self._publishing_house, self._year, self._num_pages, self._num_copies

    @book.setter
    def book(self, author, title, publishing_house, year, num_pages, num_copies):
        if type(self._author) != str or type(self._title) != str or type(self._publishing_house) != str or type(self._year) != int or type(self._num_pages) != int or type(self._num_copies) != int:
            raise TypeError
        elif self._year <= 0 or self._num_pages <= 0 or self._num_copies <= 0:
            raise ValueError
        else:
            self._author = author
            self._title = title
            self._publishing_house = publishing_house
            self._year = year
            self._num_pages = num_pages
            self._num_copies = num_copies


