# Library Management System

## Overview
This project is designed to manage a collection of books using JSON for data storage and follows Object-Oriented Programming (OOP) principles. The system allows you to add new books, view existing books, and save them to a JSON file.

### Features
- **Add New Books**: Allows users to input book details such as title, author, publication year, and genre.
- **View Books**: Displays the list of books in a table format.
- **JSON Storage**: Saves the book collection in a `library.json` file using the JSON format.

## Project Structure
- `json_handler.py`: Contains the `JsonHandler` class, which handles reading and writing JSON files.
- `book.py`: Defines the `Book` class, representing the properties of a book and its conversion to a dictionary.
- `main.py`: Implements the main logic for adding and viewing books, and integrates the JSON file handling.

## Usage Instructions

### 1. Adding a New Book
To add a new book to the library, run the program and select the option to input book details. You'll be prompted to enter the title, author, year of publication, and genre. The book will then be saved in the `library.json` file.

### 2. Viewing All Books
Choose the option to view books, and all saved books will be displayed in a table format.

### 3. Exiting the Program
To exit the program, simply choose the exit option from the menu.

## Running the Program
Make sure Python is installed, then follow these steps:

1. Install the required libraries:
   ```bash
   pip install tabulate
   ```

2. Run the program:
   ```bash
   python main.py
   ```

### Example
Here is an example of how the books are stored in `library.json`:

```json
[
    {
        "title": "El Plan Fénix",
        "author": "Brian Tracy",
        "year": 2021,
        "genre": "Personal Growth"
    },
    {
        "title": "Flow: The Psychology of Optimal Experience",
        "author": "Mihaly Csikszentmihalyi",
        "year": 1990,
        "genre": "Self-help book"
    }
]
```
---

## OOP Adaptation
The initial code was refactored to follow OOP and SOLID principles:
- **JsonHandler class**: Handles JSON file operations like writing and reading.
- **Book class**: Models a book entity with attributes (title, author, year, genre) and converts it to a dictionary for JSON serialization.

## Functions Added
- **add_book()**: Gathers book information from the user.
- **main()**: Provides a menu interface for users to add or view books.

