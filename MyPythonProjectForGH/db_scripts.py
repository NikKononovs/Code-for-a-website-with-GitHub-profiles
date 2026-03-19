import sqlite3

conn = sqlite3.connect("portfolios.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE portfolios(
    id integer primary key autoincrement,
    uuid text unique not null,
    name text not null,
    bio text not null,
    github text,
    telegram text,
    avatar text,
    skills text
)''')

conn.commit()
conn.close()