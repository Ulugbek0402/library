from apps.users.views import register, login, logout
from apps.books.views import list_books, search_by_author, add_book, edit_book, delete_book
from apps.users import admin_views
from apps.borrows.views import borrow_book, return_book, my_borrows


def admin_menu():
    while True:
        from core.database_settings import execute_query
        user_count = execute_query("SELECT COUNT(*) FROM users;", fetch="one")[0]

        print(f"""
[Admin Menu]
1. Add Book
2. Edit Book
3. Delete Book
4. View Users ({user_count})
5. View All Borrows
6. View Statistics
7. Logout""")

        choice = input("Choose: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            edit_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            admin_views.view_users()
        elif choice == "5":
            admin_views.view_borrows()
        elif choice == "6":
            admin_views.view_stats()
        elif choice == "7":
            logout()
            break


def user_menu(user_id):
    while True:
        print("""
<<<<<<< HEAD
            [User Menu])
            1. View All Books")
            2. Search Books by Author")
            3. Borrow a Book")
            4. Return a Book")
            5. My Borrowed Books")
            6. Logout""")

        choice = input("Choose: ")
        if choice == "1":
            list_books()
        elif choice == "2":
            search_by_author()
        elif choice == "3":
            borrow_book(user_id)
        elif choice == "4":
            return_book(user_id)
        elif choice == "5":
            my_borrows(user_id)
        elif choice == "6":
            logout()
            break


def auth_menu():
    while True:
        print("""

            1. Register
            2. Login
            3. Exit""")

        choice = input("Choose: ")
        if choice == "1":
            register()
        elif choice == "2":
            user_type = login()
            if user_type == "admin":
                admin_menu()
            elif isinstance(user_type, int):
                user_menu(user_type)
        elif choice == "3":
            print("Goodbye!")
            break


if __name__ == "__main__":
    auth_menu()
