"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""


class Person:
    fio: str
    phone: int

    def __init__(self, fio, phone):
        self.fio = fio
        self.phone = phone


class LibraryReader(Person):
    id: int
    books = []

    def __init__(self, fio, phone, id, books):
        super().__init__(fio, phone)
        self.id = id
        self.books = books

    def take_books(self, *args):
        for book_names in args:
            self.books.append(book_names)
        if len(args) <= 3:
            print(f"{self.fio} взял книги: {self.books}")
        else:
            print(f"{self.fio} взял {len(*args)} книги")

    def return_books(self, *args):
        for book_name in args:
            if book_name not in self.books:
                print(f"{self.fio} не брал {book_name}")
                break
            else:
                self.books.remove(book_name)
            print(f"{self.fio} вернул {args}")


person_1 = LibraryReader("killreal", 295534097, 2219, ["mqqq", "qweqwe"])

person_1.take_books('qweqwe', 'qweqsdd')
person_1.return_books('mqqq')
print(person_1.books)
person_1.return_books('kakaak')