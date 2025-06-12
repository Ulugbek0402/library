from core.database_settings import execute_query

def borrow_book(user_id):
    book_id = input("Enter book ID to borrow: ")
    existing = execute_query("SELECT id FROM borrows WHERE user_id = %s AND book_id = %s AND returned_at IS NULL;",
                             (user_id, book_id), fetch="one")
    if existing:
        print("Already borrowed and not returned.")
        return
    execute_query("INSERT INTO borrows (user_id, book_id) VALUES (%s, %s);", (user_id, book_id))
    execute_query("UPDATE books SET available_count = available_count - 1 WHERE id = %s;", (book_id,))
    print("Book borrowed.")

def return_book(user_id):
    book_id = input("Enter book ID to return: ")
    result = execute_query(
        "UPDATE borrows SET returned_at = CURRENT_TIMESTAMP WHERE user_id = %s AND book_id = %s AND returned_at IS NULL RETURNING id;",
        (user_id, book_id), fetch="one")
    if result:
        execute_query("UPDATE books SET available_count = available_count + 1 WHERE id = %s;", (book_id,))
        print("Book returned.")
    else:
        print("You haven't borrowed this book or already returned it.")

def my_borrows(user_id):
    borrows = execute_query(
        "SELECT b.id AS book_id, b.title, br.borrowed_at FROM borrows br JOIN books b ON br.book_id = b.id "
        "WHERE br.user_id = %s AND br.returned_at IS NULL ORDER BY br.borrowed_at DESC;", (user_id,), fetch="all")
    if not borrows:
        print("No active borrowed books.")
        return
    for row in borrows:
        print(f"Book ID: {row['book_id']} | {row['title']} - Borrowed: {row['borrowed_at']}")
