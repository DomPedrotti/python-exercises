from checkbook_functions import make_transaction, check_balance
#Print welcome message and show options for input selection
print("~~~~ Welcome to your Terminal Checkbook! ~~~~\n")
action = ''
while action != '4':
    print("\nWhat would you like to do? \n\n1) Check Balance\n2) Record a Debit (Make a Deposit\n3) Record a Credit (Make a Withdrawl)\n4) Exit Application")


    action = input("\nYour Choice? ")
    while action not in ['1','2','3','4']:
        action = input("Sorry, Your Selection is Invalid:\n\nPlease enter one of the following (1, 2, 3, or 4) ")

    if action == '1':
        print(f"\nYour balance is ${check_balance()}\n")

    elif action == '2':
        deposite_amount = input("\nHow much is the debit? ")
        make_transaction(deposite_amount)

    elif action == '3':
        deposite_amount = input("\nHow much is the credit? ")
        make_transaction(-1 * int(deposite_amount))

    else:
        print "\nThanks and have a great day!"
        break
