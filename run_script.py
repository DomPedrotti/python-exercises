def make_deposite(amt):
    """Make """
    import csv
    fields = [amt]
    with open(r'transactions.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

def check_balance():
    """check_balance() takes no arguments and returns the sum of transactions.csv"""
    import csv
    with open("transactions.csv") as file:
        balance = 0
        for row in csv.reader(file):
            balance += int(row[0])
    return balance

print(check_balance())