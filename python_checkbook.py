import csv
from checkbook_functions import check_balance, add_description, update_sql_table, select_all, print_table, search_by_date, search_by_category, search_by_keyword
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
        action = input("Sorry, Your Selection is Invalid:\n\nPlease enter one of the following (1, 2, 3, 4, or 5) ")

    if action == '1':
        print(f"\nYour balance is ${check_balance()}")
        input("press <ENTER> to continue")


    elif action == '2' or action == '3':
        if action == '2':    
            amount = input("\nHow much is the debit? ")
        else:
            amount = input("\nHow much is the credit? ")
            amount = int(amount) * -1
        category = input("what is this transaction category? ")
        description = add_description()
        time = time()
        update_sql_table(time, amount, category, description)

    elif action == '4':
        view_history = input('Would you like to...\n\n1) See All Transactions\n2) Filter Search\n')
        
        if view_history.strip() == '1':
            table = select_all()
            print_table(table)
        else: 
            search_by = input("Would You Like to... \n1) Search by Date \n2) Search by Category \n3) Search by Key Word?\n")
            if search_by == '1':
                table = search_by_date()
                print_table(table)
            elif search_by == '2':
                table = search_by_category()
                print_table(table)
            else:
                table = search_by_keyword()
                print_table(table)



    elif action == '5':
        print("\nThanks and have a great day!\n")
        break
