import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL,
             password TEXT NOT NULL
             )''')

c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'adminpassword'))
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user', 'userpassword'))

conn.commit()
conn.close()

def login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    user = c.fetchone()
    conn.close()

    return user

def main():
    print("Welcome to the SQL Injection Game!")
    print("Try to login as admin without knowing the password!")

    attempts = 0  # Initialize attempts counter

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = login(username, password)

        if user:
            print("Login successful!")
            print(f"Welcome, {user[1]}!")
            break
        else:
            print("Login failed. Try again.")
            attempts += 1  # Increment attempts counter

    print(f"Number of attempts: {attempts}")

if __name__ == "__main__":
    main()
