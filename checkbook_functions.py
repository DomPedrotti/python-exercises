def check_balance():
    '''
    check_balance() takes no arguments and returns the sum of transactions.csv
    '''
    import csv
    with open("transactions.csv") as file:
        balance = 0
        for row in csv.reader(file):
            balance += float(row[0])
    return balance


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
        
def print_table():
    print ('*------------------------------------------------------------------------*')
    print ('|Date          |Amount    |Category       |Description                   |')
    print ('*------------------------------------------------------------------------*')
    

def update_sql_table():
    import pymysql




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



