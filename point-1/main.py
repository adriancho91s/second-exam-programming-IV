from json_handler import JsonHandler
from book import Book
from tabulate import tabulate


def add_book():
    """
    Prompts the user to enter book details and creates a new Book instance.

    Returns:
        Book: A new book instance with the provided details.
    """
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    while True:
        try:
            year = int(input("Enter the publication year of the book: "))
            break
        except ValueError:
            print("Please enter a valid year.")
    genre = input("Enter the genre of the book: ")
    return Book(title, author, year, genre)


def main():
    books = []
    file_path = "library.json"

    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Print all books")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book = add_book()
            books.append(book.to_dict())
            JsonHandler.write(file_path, books)
        elif choice == "2":
            read_data = JsonHandler.read(file_path)
            if read_data:
                print("Books in the library:")
                print(tabulate(read_data, headers="keys"))
            else:
                print("No books found in the library.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
