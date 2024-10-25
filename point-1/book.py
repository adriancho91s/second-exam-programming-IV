class Book:
    """
    A class to represent a book.
    """

    def __init__(self, title, author, year, genre):
        """
        Initializes a new book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def to_dict(self):
        """
        Converts the book instance to a dictionary.

        Returns:
            dict: The book instance as a dictionary.
        """
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre
        }
