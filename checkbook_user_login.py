from pick import pick
from cb_sql_functions import select_usernames, check_password, add_new_user_table



def log_on():
    existing_user = new_or_existing_user()
    if existing_user == None:
        return
    elif existing_user:
        return enter_user_and_password()
    elif not existing_user:
        create_account()
        return enter_user_and_password()
    


def new_or_existing_user():
    prompt = "Are You a New or Exising User? (Use Arrow Keys to Make Selection)"
    choices = ['Current User', 'New User', 'Exit']
    identify, index = pick(choices, prompt, indicator = '->')
    
    if index == 2:
        return None
    elif index == 0:
        return True
    else:
        return False


def enter_user_and_password():
    print("Please Enter Login Information: ")
    all_usernames = select_usernames()
    username = input('Username: ')
    while username not in all_usernames:
        error = 'Invalid Username, Try Again?'
        choices = ['Yes', 'No']
        choice, index = pick(choices, error)
        if index == 1:
            return
        else:
            username = input('Username: ')
    password = input('Password: ')
    while not check_password(username, password):
        error = 'Invalid Password, Try Again?'
        choices = ['Yes', 'No']
        choice, index = pick(choices, error)
        if index == 1:
            return
        else:
            password = input('Password: ')
    return username

def create_account():
    username = input('New Username: ')
    password = input('Password: ')
    add_new_user_table(username, password)
    Print("\n Congratulations, you're all set!\n")



