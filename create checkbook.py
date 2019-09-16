import sqlite3
conn = sqlite3.connect('checkbook.db')
c = conn.cursor()

c.execute("CREATE TABLE usernames (username text)")

conn.close()