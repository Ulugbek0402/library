# 📚 Kutubxona Project (Library Management System)

A simple terminal-based library management system written in Python and PostgreSQL using `psycopg2`.

---

## 🚀 Features

### 👤 User Menu:
- View all available books
- Search books by author
- Borrow a book
- Return a book
- View your borrow history

### 🛠 Admin Menu:
- Add a book and its author (automatically saves new authors)
- Edit book details (title and author)
- Delete books
- View user count and list
- View borrow records
- View system statistics

---

## 🧱 Database Schema

Tables:
- `authors(id, full_name)`
- `books(id, title, author_id, published_at, total_count, available_count)`
- `users(id, full_name, email)`
- `borrows(id, user_id, book_id, borrowed_at, returned_at)`

---

## ⚙️ Technologies Used
- Python 3
- PostgreSQL
- `psycopg2`
- `python-dotenv`

---

