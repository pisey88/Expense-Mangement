import sqlite3
from collections import defaultdict

class Database:
    def __init__(self, db_name="expenses.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)

        # Create expenses table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                note TEXT,
                FOREIGN KEY (username) REFERENCES users(username)
            )
        """)

        self.conn.commit()

    def save_users_data(self, users_data):
         try:
             for username, password in users_data.items():
                 self.cursor.execute("INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)", (username, password))
             self.conn.commit()
         except sqlite3.Error as e:
                print(f"Database error: {e}")


    def load_users_data(self):
        self.cursor.execute("SELECT * FROM users")
        users_data = self.cursor.fetchall()
        return {username: password for username, password in users_data}

    def save_expense_data(self, username, expenses):
        # Delete existing expenses for the user before adding new ones
        self.cursor.execute("DELETE FROM expenses WHERE username = ?", (username,))
        for expense in expenses:
            self.cursor.execute("INSERT INTO expenses (username, name, category, amount, date, note) VALUES (?, ?, ?, ?, ?, ?)",
                                (username, expense['name'], expense['category'], expense['amount'], expense['date'], expense['note']))
        self.conn.commit()

    def load_expense_data(self, username):
        self.cursor.execute("SELECT name, category, amount, date, note FROM expenses WHERE username = ?", (username,))
        expenses_data = self.cursor.fetchall()
        expenses = [{"name": name, "category": category, "amount": amount, "date": date, "note": note}
                   for name, category, amount, date, note in expenses_data]
        return expenses


    def close(self):
        self.conn.close()
