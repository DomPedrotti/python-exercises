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


def make_transaction(amount,category,timestamp):
    '''
    make_transaction() takes in transaction amount, category and the time the transaction was maded and stores them in transactions.csv
    '''
    import csv
    fields = [amount, category, timestamp]
    with open(r'transactions.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    pass


# def make_withdrawl(amt):
#     import csv
#     fields = [-amt]
#     with open(r'transactions.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(fields)
#     pass
