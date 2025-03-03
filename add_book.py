from book import Book
from book_data import load_books, save_books

def add_book():
    """Adds a new book to the bookstore."""
    books = load_books()
    
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author: ").strip()
    isbn = input("Enter ISBN (Unique ID): ").strip()
    genre = input("Enter Genre: ").strip()

    try:
        price = float(input("Enter Price: "))
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        
        quantity = int(input("Enter Quantity in Stock: "))
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        # Check for duplicate ISBN
        if any(book.isbn == isbn for book in books):
            print("❌ Error: A book with this ISBN already exists!")
            return

        new_book = Book(title, author, isbn, genre, price, quantity)
        books.append(new_book)
        save_books(books)
        print("✅ Book added successfully!")

    except ValueError as e:
        print(f"❌ Error: {e}")
