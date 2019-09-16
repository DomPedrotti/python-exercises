# def check_balance():
    # '''
    # check_balance() takes no arguments and returns the sum of transactions.csv
    # '''
    # import csv
    # with open("transactions.csv") as file:
    #     balance = 0
    #     for row in csv.reader(file):
    #         balance += float(row[0])
    # return balance

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
        amount_col = str(i[1]) + (10-len(str(i[1]))) *' ' + '|'
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
