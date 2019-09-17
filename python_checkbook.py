from checkbook_user_login import log_on
from cb_sql_functions import update_sql_table, select_all, search_by_date, search_by_category, search_by_keyword
from checkbook_functions import check_balance, add_description, print_table, check_value, pick_one
from time import time
from pick import pick 
username = log_on()
#prompt username and open associated table
### username = check_username()

#Print welcome message and show options for input selection
print("~~~~ Welcome to your Terminal Checkbook! ~~~~\n")
while True:
    options = ('1) Check Balance', '2) Make a Deposit', '3) Make a Withdrawl', '4) Search History', '5) Exit')
    print(f"\nWhat would you like to do? \n\n{options[0]} \n{options[1]} \n{options[2]} \n{options[3]} \n{options[4]}")
    action = input("\nYour Choice? ")
    
    if action not in ['1', '2', '3', '4', '5']:
        choice, action = pick_one(options)

    if action == '1':
        print(f"\nYour balance is ${check_balance()}")
        input("press <ENTER> to continue")

    elif action == '2' or action == '3':
        if action == '2':    
            amount = input("\nHow Much Would You Like to Deposite? ")
            check_value(amount)
                   
        else:
            amount = input("\nHow Much Would You Like to Withdrawl? ")
            check_value(amount)
            amount = float(amount) * -1
        category = input("what is this transaction category? ")
        description = add_description()
        time = time()
        update_sql_table(time, amount, category, description, username)

    elif action == '4':
        view_history = input('Would you like to...\n\n1) See All Transactions\n2) Filter Search\n')
        
        if view_history not in ('1', '2'):
            choice, view_history = pick_one(['1) See All Transactions', '2) Filter Search'])

        if view_history.strip() == '1':
            table = select_all(username)
            print_table(table)
        else: 
            search_by = input("Would You Like to... \n1) Search by Date \n2) Search by Category \n3) Search by Key Word?\n")
            
            if search_by not in ['1', '2', '3']:
                choice, search_by = pick_one(['1) Search by Date' ,'2) Search by Category', '3) Search by Key Word?'])
            
            if search_by == '1':
                table = search_by_date(username)
                print_table(table)
            elif search_by == '2':
                table = search_by_category(username)
                print_table(table)
            elif search_by == '3':
                table = search_by_keyword(username)
                print_table(table)

    elif action == '5':
        print("\nThanks and have a great day!\n")
        break
    

