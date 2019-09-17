import sqlite3
conn = sqlite3.connect('checkbook.db')
c = conn.cursor()

#c.execute("CREATE TABLE users (username text, password text)")

#create table
#c.execute('''
#CREATE TABLE stocks
#(date text, trans text, symbol text, qty real, price real) ''')

#insert row
#c.execute("insert into users values ('dom', '     ')")
# #save changes
#conn.commit()



#c.execute("insert into users values ('jon', 'jon')")
# #close connection
#conn.close()

#conn = sqlite3.connect('checkbook.db')
#c = conn.cursor()

c.execute("DROP TABLE jon;")
conn.commit()
#show row
for row in c.execute('SELECT * FROM users'):
    print(row)

conn.close()