import csv
from checkbook_functions import make_transaction, check_balance, add_description, update_sql_table
from time import time, sleep

#prompt username and open associated table
### username = check_username()

#Print welcome message and show options for input selection
print("~~~~ Welcome to your Terminal Checkbook! ~~~~\n")
action = ''
while action != '5':
    print("\nWhat would you like to do? \n\n1) Check Balance\n2) Record a Debit (Make a Deposit\n3) Record a Credit (Make a Withdrawl)\n4) Search History\n5) Exit Application")


    action = input("\nYour Choice? ")
    while action not in ['1','2','3','4','5']:
        action = input("Sorry, Your Selection is Invalid:\n\nPlease enter one of the following (1, 2, 3, or 4) ")

    if action == '1':
        print(f"\nYour balance is ${check_balance()}")
        input("press <ENTER> to continue")


    elif action == '2' or action == '3':
        if action == '2':    
            amount = input("\nHow much is the debit? ")
        else:
            amount = input("\nHow much is the credit? ")
            amount = int(amount) * -1
        category = input("what is this transaction for? ")
        description = add_description()
        time = time()
        update_sql_table(time, amount, category, description)

    elif action == '4':
        input('Would you like to...\a\a1) See All Transactions\n2) Filter Search')
        
    elif action == '5':
        print("\nThanks and have a great day!\n")
        break
