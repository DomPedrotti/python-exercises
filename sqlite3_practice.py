import sqlite3
# conn = sqlite3.connect('checkbook.db')
# c = conn.cursor()

#c.execute("CREATE TABLE usernames (username text)")

#create table
#c.execute('''
#CREATE TABLE stocks
#(date text, trans text, symbol text, qty real, price real) ''')

#insert row
# c.execute("insert into usernames values ('dom')")
# #save changes
# conn.commit()




# #close connection
# conn.close()

conn = sqlite3.connect('checkbook.db')
c = conn.cursor()



#show row
for row in c.execute('SELECT * FROM dom'):
    print(type(row[0]))

conn.close()