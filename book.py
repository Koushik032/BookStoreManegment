class Book:
    # Represents a book in the bookstore.
    
    def __init__(self, title, author, isbn, genre, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        # Converts the Book object into a dictionary format for storage.
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(book_dict):
        # Creates a Book object from a dictionary.
        return Book(
            book_dict["title"],
            book_dict["author"],
            book_dict["isbn"],
            book_dict["genre"],
            book_dict["price"],
            book_dict["quantity"]
        )
