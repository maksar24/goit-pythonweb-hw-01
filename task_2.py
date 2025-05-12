from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):

    def __init__(self) -> None:
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        book = next((b for b in self._books if b.title == title), None)
        if book:
            self._books.remove(book)
            logger.info(f"Book with title '{title}' removed.")
        else:
            logger.warning(f"No book with title '{title}' was found to remove.")

    def get_books(self) -> List[Book]:
        return self._books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> List[Book]:
        books = self.library.get_books()
        if not books:
            logger.info("No books in the library.")
        for book in books:
            logger.info(str(book))
        return books


def main() -> None:
    library: LibraryInterface = Library()
    manager: LibraryManager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year_input = input("Enter book year: ").strip()

                try:
                    year = int(year_input)
                except ValueError:
                    logger.error("Invalid year input. Please enter a valid number.")
                    continue

                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting program.")
                break

            case _:
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
