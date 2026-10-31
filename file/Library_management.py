class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def show_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

    def get_number_of_books(self):
        print("Total number of books:", self.no_of_books)


# Creating library object
l1 = Library()

# Adding books
l1.add_book("Python")
l1.add_book("Java")
l1.add_book("C++")
l1.add_book("Data Structure")
l1.add_book("political science")
# Displaying all books
l1.show_books()

# Displaying number of books
l1.get_number_of_books()