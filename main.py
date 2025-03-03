from add_book import add_book
from view_books import view_books
from search_book import search_book
from delete_book import remove_book

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n📚 Book Store Management System")
        print("=" * 40)
        print("1️⃣ Add a Book")
        print("2️⃣ View All Books")
        print("3️⃣ Search for a Book")
        print("4️⃣ Remove a Book")
        print("5️⃣ Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("📌 Exiting the system... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
