import sqlite3

# Connect to SQLite database (this will create a new file if it doesn't exist)
connection = sqlite3.connect('donation.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cash INTEGER DEFAULT 0,
    full_name TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
''')

# Create the charities table
cursor.execute('''
CREATE TABLE IF NOT EXISTS charities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    website TEXT NOT NULL,
    contact_email TEXT,
    description TEXT,
    share_price INTEGER NOT NULL DEFAULT 100
);
''')

# Create the donations table
cursor.execute('''
CREATE TABLE IF NOT EXISTS donations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    charityID INTEGER NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userID) REFERENCES users (id),
    FOREIGN KEY (charityID) REFERENCES charities (id)
);
''')

# Commit the changes and close the connection
connection.commit()
connection.close()
