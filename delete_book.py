from book_data import load_books, save_books

def remove_book():
    """Removes a book by its ISBN."""
    books = load_books()
    
    isbn = input("Enter ISBN of the book to remove: ").strip()
    
    for book in books:
        if book.isbn == isbn:
            books.remove(book)
            save_books(books)
            print("✅ Book removed successfully!")
            return
    
    print("❌ Error: No book found with the given ISBN!")
