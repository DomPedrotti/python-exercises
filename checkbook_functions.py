def CSV_check_balance():
    '''
    check_balance() takes no arguments and returns the sum of transactions.csv
    '''
    import csv
    with open("transactions.csv") as file:
        balance = 0
        for row in csv.reader(file):
            balance += float(row[0])
    return balance

def check_balance():
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    c = conn.cursor()

    rows = []
    for row in c.execute('SELECT amount FROM dom'):
        rows.append(row[0])
    return sum(rows)

    conn.close()

def make_transaction(amount,category,description,timestamp):
    '''
    make_transaction() takes in transaction amount, category and the time the transaction was maded and stores them in transactions.csv
    '''
    import csv
    fields = [amount, category, description, timestamp]
    with open(r'transactions.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    pass

def add_description():
    '''
    Prompts user to add description
    
    returns user input for description if user opts to add one

    else returns 'n/a'
    '''
    prompt_input = input("Would You Like to Add a Description? (y/n) ")
    while prompt_input.lower() not in ['y','n']:
        prompt_input = input("Invalid Response, Please Enter 'y' for Yes or 'n' for No ")
    
    if prompt_input.lower() == 'y':
        return input("Please Enter Description. \n")
        
    else:
        print('~No Description~')
        return 'n/a'
        
def print_table(raw_table):
    print ('*------------------------------------------------------------------------*')
    print ('|Date          |Amount    |Category       |Description                   |')
    print ('*------------------------------------------------------------------------*')
    for i in raw_table:
        date_col = '|' + date_from_timestamp(float(i[0])) + '|'
        # print((10-len(str(i[1])) *' '))
        amount_col = (10-len(str(i[1]))) * ' ' + str(i[1]) + '|'
        category_col = i[2] + (15-len(i[2])) * ' ' + '|'
        description = string_wrap_text(i[3], 30).split('\n')
        description_col = description[0] + (30-len(description[0])) * ' ' + '|'
        print(date_col + amount_col + category_col+ description_col )
        for i in description[1:]:
            print('|              |          |               |' + i + (30 -len(i)) * ' ' +'|')
        print ('*------------------------------------------------------------------------*')

def check_username():
    import pymysql
    new_or_existing_user = input('Are you an existing user? (y/n) ')
    #**add while to check input later
    if new_or_existing_user.strip().lower() == 'y':
        username = input('please Enter Username\n')
    #**add while to verify real user
        return username
    else:
        new_username = input('please enter username')
        
    #**add while to check if username already taken
        add_new_user_table(new_username)
        return new_username


def update_sql_table(time, amount, category, description):
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    
    c = conn.cursor()

    transaction = (time, amount, category, description,)
    c.execute("INSERT INTO dom VALUES (?,?,?,?)", transaction)

    conn.commit()

    conn.close()


def add_new_user_table(user):
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    c = conn.cursor()

    c.execute("CREATE TABLE " + user + " (date text, amount real, Category text, description text)")

    c.execute("insert into usernames values("+user+")")

    conn.close()

def select_all():
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    c = conn.cursor()

    table = []
    for row in c.execute("SELECT * FROM dom"):
        table.append(row)
    conn.close()
    return table

def search_by_date():
    start_date = input("Enter Start Date (MM/DD/YYYY) ")
    end_date = input("Enter End Date (MM/DD/YYYY) ")
    date_range = (timestamp_from_date(start_date), timestamp_from_date(end_date) + 86400)
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    c = conn.cursor()

    table = []
    for row in c.execute("SELECT * FROM dom WHERE date BETWEEN ? and ?", date_range):
        table.append(row)
    conn.close()
    return table

def search_by_category():
    choose_category = input("Type 'D' to see Deposits and 'W' to see Withdrawals")
    while True:
        if choose_category.lower() in ['w', 0]:
            category = 'Withdrawal'
            break
        elif choose_category.lower() in ['d', 1]:
            category = 'Deposit'
            break
        else:
            category, choose_category = pick_one(['Deposit', 'Withdrawal'])
            break
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    c = conn.cursor()

    table = []
    for row in c.execute("SELECT * FROM dom WHERE Category = ?", [category]):
        table.append(row)
    conn.close()
    return table

def search_by_keyword():
    keyword = input('Enter Keyword ')
    import sqlite3
    conn = sqlite3.connect('checkbook.db')
    c = conn.cursor()

    table = []
    for row in c.execute("SELECT * FROM dom WHERE description LIKE '%" +keyword+"%'"):
        table.append(row)
    conn.close()
    return table

def timestamp_from_date(date):
    import time
    from datetime import datetime
    timestamp = datetime(int(date[-4:]), int(date[:2]), int(date[3:5]), 0, 0).timestamp()
    return timestamp

def date_from_timestamp(timestamp):
    from datetime import date, datetime
    ugly_date = datetime.fromtimestamp(timestamp)
    pretty_date = str(ugly_date)[5:7] + '/' + str(ugly_date)[8:10] + '/' + str(ugly_date)[2:4]
    #print(str(ugly_date)[11:16])
    time = str(ugly_date)[11:16]
    return pretty_date + ' ' + time

def string_wrap_text(string, width):
    word_list = string.split(' ')
    return_string = ''
    running_len = 0
    for i in word_list:
        if len(return_string + i) - running_len < width:
            return_string += (i + ' ')
        else:
            return_string += ('\n' + i + ' ') 
            running_len = len(return_string)-len('\n' + i + ' ')
    return return_string

def check_value(value):
    value = check_valid_number(value)
    while float(value) > 50000 and float(value) >= 0:
        value = input("\nWe Do Not Accept Withdrawls or Deposits \nof Greater Than 50,000 at a Time, \n\nPlease Enter A Value of Up to 50,000.00 ")
        value = check_valid_number(value)

def pick_one(choices):
    from pick import pick
    ask = "Sorry, Your Selection is Invalid,\n\nPlease Select One of the Following:"
    selection, index = pick(choices, ask, indicator = '->')
    return selection, str(index + 1)

def check_valid_number(value):
    while True:
        try:
            float(value)
            break
        except(ValueError):
            value = input('Please Enter a Valid, Positive Number ')
            continue
    return value