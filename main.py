import sys
from models import Book, Library

def print_menu():
    print("\n" + "="*35)
    print("      МЕНЮ - ГРАДСКА БИБЛИОТЕКА")
    print("="*35)
    print("1. Добави нова книга")
    print("2. Покажи всички книги")
    print("3. Сортирай книгите по година")
    print("4. Изход")
    print("="*35)

def main():
    my_library = Library("Градска Библиотека")
    
    print("Добре дошли в системата за управление на библиотеката!")

    while True:
        print_menu()
        choice = input("Моля, изберете опция (1-4): ").strip()

        if choice == "1":
            print("\n--- Добавяне на нова книга ---")
            title = input("Въведете заглавие: ").strip()
            author = input("Въведете автор: ").strip()
            
            while True:
                year_input = input("Въведете година на издаване: ").strip()
                if year_input.isdigit():
                    year = int(year_input)
                    break
                else:
                    print("Грешка: Моля, въведете валидно число за година!")

            new_book = Book(title, author, year)
            my_library.add_book(new_book)

        elif choice == "2":
            my_library.display_books()

        elif choice == "3":
            my_library.sort_books_by_year()

        elif choice == "4":
            print("\nБлагодарим ви, че използвахте системата! Довиждане.")
            sys.exit()

        else:
            print("\nНевалиден избор! Моля, въведете цифра от 1 до 4.")

if __name__ == "__main__":
    main()