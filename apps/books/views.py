from core.database_settings import execute_query


def list_books():
    books = execute_query(
        "SELECT b.id, b.title, a.full_name AS author, b.available_count FROM books b JOIN authors a ON b.author_id = a.id;",
        fetch="all")
    for book in books:
        print(f"{book['id']}: {book['title']} by {book['author']} (Available: {book['available_count']})")


def search_by_author():
    author = input("Enter author name: ")
    books = execute_query(
        "SELECT b.id, b.title FROM books b JOIN authors a ON b.author_id = a.id WHERE a.full_name ILIKE %s;",
        (f"%{author}%",), fetch="all")
    for book in books:
        print(f"{book['id']}: {book['title']}")


def add_book():
    title = input("Title: ")
    author_name = input("Author full name: ")
    published_at = input("Published year (YYYY-MM-DD): ")
    total_count = int(input("Total count: "))
    available_count = total_count

    author = execute_query("SELECT id FROM authors WHERE full_name = %s;", (author_name,), fetch="one")
    if not author:
        author = execute_query("INSERT INTO authors (full_name) VALUES (%s) RETURNING id;", (author_name,), fetch="one")
        if not author:
            print("Failed to add author.")
            return

    author_id = author['id']
    result = execute_query(
        "INSERT INTO books (title, author_id, published_at, total_count, available_count) "
        "VALUES (%s, %s, %s, %s, %s) RETURNING id;",
        (title, author_id, published_at, total_count, available_count),
        fetch="one"
    )

    if result:
        print(" Book added successfully.")
    else:
        print(" Failed to add book to database.")


def edit_book():
    book_id = input("Enter book ID: ")
    title = input("New title: ")
    author_name = input("New author name: ")
    author = execute_query("SELECT id FROM authors WHERE full_name = %s;", (author_name,), fetch="one")
    if not author:
        author = execute_query("INSERT INTO authors (full_name) VALUES (%s) RETURNING id;", (author_name,), fetch="one")
    author_id = author['id']
    execute_query("UPDATE books SET title = %s, author_id = %s WHERE id = %s;", (title, author_id, book_id))
    print("Book updated.")


def delete_book():
    book_id = input("Enter book ID: ")
    try:
        result = execute_query(
            "DELETE FROM books WHERE id = %s RETURNING id;",
            (book_id,), fetch="one"
        )
        if result:
            print(f" Book with ID {book_id} deleted.")
        else:
            print(" Book not found or could not be deleted (maybe it's borrowed).")
    except Exception as e:
        print(f" Error deleting book: {e}")

