from prettytable import PrettyTable

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Успех: Книгата '{book.title}' е добавена в библиотеката!")

    def display_books(self):
        if not self.books:
            print("Библиотеката е празна.")
            return
        
        table = PrettyTable(["Заглавие", "Автор", "Година на издаване"])
        for book in self.books:
            table.add_row([book.title, book.author, book.year])
        
        print(f"\n--- Налични книги в {self.name} ---")
        print(table)

    def sort_books_by_year(self):
        n = len(self.books)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.books[j].year > self.books[j + 1].year:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]
        print("\nУспех: Книгите са сортирани по година на издаване!")