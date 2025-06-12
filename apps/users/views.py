from core.database_settings import execute_query


def register():
    email = input("Enter email: ")
    full_name = input("Enter full name: ")
    existing = execute_query("SELECT * FROM users WHERE email = %s;", (email,), fetch="one")
    if existing:
        print("Email already registered.")
        return
    execute_query("INSERT INTO users (email, full_name) VALUES (%s, %s);", (email, full_name))
    print("Registration successful.")


def login():
    email = input("Enter your email: ")
    if email == "admin@admin.com":
        password = input("Enter password: ")
        if password == "admin":
            print("Admin login successful.")
            return "admin"
    result = execute_query("SELECT id FROM users WHERE email = %s;", (email,), fetch="one")
    if result:
        print("Login successful.")
        return result[0]
    print("No such user.")
    return None


def logout():
    print("Logged out.")
