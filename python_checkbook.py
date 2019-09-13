from checkbook_functions import make_transaction, check_balance
from time import time
#Print welcome message and show options for input selection
print("~~~~ Welcome to your Terminal Checkbook! ~~~~\n")
action = ''
while action != '5':
    print("\nWhat would you like to do? \n\n1) Check Balance\n2) Record a Debit (Make a Deposit\n3) Record a Credit (Make a Withdrawl)\n4) See History\n5) Exit Application")


    action = input("\nYour Choice? ")
    while action not in ['1','2','3','4','5']:
        action = input("Sorry, Your Selection is Invalid:\n\nPlease enter one of the following (1, 2, 3, or 4) ")

    if action == '1':
        print(f"\nYour balance is ${check_balance()}\n")

    elif action == '2':
        deposite_amount = input("\nHow much is the debit? ")
        deposite_category = input("what is this transaction for? ")
        deposite_time = time()
        make_transaction(deposite_amount,deposite_category,deposite_time)

    elif action == '3':
        withdrawl_amount = input("\nHow much is the credit? ")
        withdrawl_category = input("what is this transaction for? ")
        withdrawl_time = time()
        make_transaction(-1 * int(withdrawl_amount), withdrawl_category,withdrawl_time)

    elif action == '5':
        print("\nThanks and have a great day!\n")
        break
