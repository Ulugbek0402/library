from core.database_settings import execute_query

def view_users():
    users = execute_query("SELECT id, full_name, email FROM users;", fetch="all")
    if not users:
        print("No users found.")
        return
    for user in users:
        print(f"ID: {user['id']} - Name: {user['full_name']} - Email: {user['email']}")

def view_borrows():
    borrows = execute_query(
        "SELECT br.id, u.full_name AS user_name, b.title, br.borrowed_at, br.returned_at "
        "FROM borrows br JOIN users u ON br.user_id = u.id JOIN books b ON br.book_id = b.id;", fetch="all")
    if not borrows:
        print("No borrow records found.")
        return
    for row in borrows:
        print(f"Borrow ID: {row['id']} | {row['user_name']} borrowed '{row['title']}' at {row['borrowed_at']} - Returned: {row['returned_at']}")

def view_stats():
    books = execute_query("SELECT COUNT(*) FROM books;", fetch="one")[0]
    users = execute_query("SELECT COUNT(*) FROM users;", fetch="one")[0]
    borrows = execute_query("SELECT COUNT(*) FROM borrows;", fetch="one")[0]
    print(f"Total books: {books}, Users: {users}, Borrow events: {borrows}")
