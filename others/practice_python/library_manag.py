class Library:
    def __init__(self, name):
        self.name = name              # Store the library name
        self.no_of_books = 0
        self.total_books = []

    def add_book(self, book):
        self.total_books.append(book)
        self.no_of_books = len(self.total_books)
        print(f"Book '{book}' added. Total books now: {self.no_of_books}")

    def show(self):
        print(f"\nThe number of books in {self.name} library: {self.no_of_books}")
        print("Books list:")
        for book in self.total_books:
            print(f"- {book}")

# Usage
library_name = "Milinds"
l1 = Library(library_name)

n = int(input("Enter the number of books you want to add: "))
for i in range(1, n + 1):
    book_name = input(f"Enter the name of book {i}: ")
    l1.add_book(book_name)

l1.show()