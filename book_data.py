import json
import os
from book import Book

BOOKS_FILE = "data/bookstore.json"

def load_books():
    """Loads books from a file if available, else returns an empty list."""
    if not os.path.exists(BOOKS_FILE):
        return []  # If file does not exist, return an empty list
    
    with open(BOOKS_FILE, "r") as file:
        try:
            books_data = json.load(file)  # Try to load JSON
            return [Book.from_dict(book) for book in books_data]
        except (json.JSONDecodeError, ValueError):  
            return []  # If file is empty or corrupted, return empty list

def save_books(books):
    """Saves the current list of books to a file."""
    os.makedirs("data", exist_ok=True)  # Ensure 'data' folder exists
    with open(BOOKS_FILE, "w") as file:
        json.dump([book.to_dict() for book in books], file, indent=4)
