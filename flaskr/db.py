import sqlite3

DATEBASE = 'bookdate.db'

def create_book_table():
    con = sqlite3.connect(DATEBASE)
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)")
    con.close()