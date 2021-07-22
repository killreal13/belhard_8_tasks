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

    def __init__(self, author, title, puplishing_house, year, num_pages, num_copies):
        self.author = author
        self.title = title
        self.publishing_house = puplishing_house
        self.year = year
        self.num_pages = num_pages
        self.num_copies = num_copies

    def __eq__(self, other):
        return self._year == other._year

    def __lt__(self, other):
        return self._year < other._year

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise TypeError
        else:
            self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError
        else:
            self._title = title

    @property
    def publishing_house(self):
        return self._publishing_house

    @publishing_house.setter
    def publishing_house(self, publishing_house):
        if not isinstance(publishing_house, str):
            raise TypeError
        else:
            self._publishing_house = publishing_house

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError
        elif year <= 0:
            raise ValueError
        else:
            self._year = year

    @property
    def num_pages(self):
        return self._num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        if not isinstance(num_pages, int):
            raise TypeError
        elif num_pages <= 0:
            raise ValueError
        else:
            self._num_pages = num_pages

    @property
    def num_copies(self):
        return self._num_copies

    @num_copies.setter
    def num_copies(self, num_copies):
        if not isinstance(num_copies, int):
            raise TypeError
        elif num_copies <= 0:
            raise ValueError
        else:
            self._num_copies = num_copies









