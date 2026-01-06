# Library System using OOP

class Book:
    """Represents a book with title and author."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    """Library class that manages a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        """Adds a new book to the library."""
        self.books.append(Book(title, author))
        print(f"✅ '{title}' by {author} added to the library.")

    def view_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("📚 No books available in the library.")
        else:
            print("\n📖 Books in Library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def remove_book(self, index):
        """Removes a book from the library by its index."""
        if 0 < index <= len(self.books):
            removed_book = self.books.pop(index - 1)
            print(f"❌ Removed: {removed_book}")
        else:
            print("⚠️ Invalid book number. Please try again.")


def main():
    """Menu-driven Library System."""
    library = Library()

    while True:
        print("\n📚 Library System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.view_books()
            try:
                index = int(input("Enter book number to remove: "))
                library.remove_book(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            print("📕 Exiting Library System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select a valid option.")


# Run the program
if __name__ == "__main__":
    main()
