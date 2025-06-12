

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT REFERENCES authors(id),
    published_at DATE,
    total_count INT,
    available_count INT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE borrows (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    book_id INT REFERENCES books(id),
    borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    returned_at TIMESTAMP
);
