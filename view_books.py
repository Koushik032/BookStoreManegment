from book_data import load_books

def view_books():
    # Displays all available books in the store.
    books = load_books()
    
    if not books:
        print("No books available in the store!")
        return

    print("Available Books:")
    print("=" * 50)
    for book in books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"ISBN: {book.isbn}")
        print(f"Genre: {book.genre}")
        print(f"Price: ${book.price:.2f}")
        print(f"Quantity: {book.quantity} in stock")
        print("=" * 50)
