from book_data import load_books

def search_book():
    """Searches for books by title or ISBN."""
    books = load_books()
    search_query = input("Enter Book Title or ISBN to search: ").strip().lower()
    
    found_books = [book for book in books if search_query in book.title.lower() or search_query == book.isbn]
    
    if not found_books:
        print("❌ No matching books found!")
        return
    
    print("\n🔍 Search Results:")
    print("=" * 50)
    for book in found_books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"ISBN: {book.isbn}")
        print(f"Genre: {book.genre}")
        print(f"Price: ${book.price:.2f}")
        print(f"Quantity: {book.quantity} in stock")
        print("=" * 50)
