from curses.ascii import CR
from hashlib import new
from re import T

from paramiko import PasswordRequiredException
from app_classes import User
from app_classes import Credentials

def display():
	print("               ____      G.R.I.T            _____  _                               ")
	print("              |  _ \ Greatness Requires    / ____|| |                              ")
	print("              | |_) ) Intenal Toughness!  / ____  | |__    _____  _ _  ____        ")
	print("              |  __/  / _  |/ __  / __    \___  \ |  __)  /  _  \| '_|/ __ \       ")
	print("              | |    / (_| |\__ \ \__ \    ___  / | |___ (  (_)  ) | |  ___/       ")
	print("              |_|    \_____| ___/  ___/   |____/  |_____) \_____/|_|  \____        ")
display()

def new_user_creation(username, password):
    '''
    To create a new user with a user name and password
    '''
    new_user = User(username, password)
    return new_user


def store_user(user):
    '''
    To store the a newly created user
    '''
    user.store_user()

def user_display():
    '''
    To show an existing user
    '''
    return User.user_display()

def user_login(username,password):
    '''
    To find out if a user exists and upon existance, it logins the user
    '''
    user_check = Credentials.user_verification(username,password)
    return user_check

def new_user_credentials(username, password, account):
    '''
    To create new credentials for a specific user account
    '''
    new_userCredentials = Credentials(username, password, account)
    return new_userCredentials

def save_new_credentials(account, username, password):
    '''
    To save new credentials to the credentials list
    '''
    Credentials.store_details(account, username, password)

def account_details_display():
    '''
    To display all details saved about all saved accounts
    '''
    return Credentials.show_credentials()

def credentials_delete(credentials):
    '''
    To delete a credential from the credentials list
    '''
    credentials.delete_details()

def credentials_search(account):
    '''
    To search for credentials using an account and returns the found credentials
    '''
    return Credentials.credentials_search(account)

def credentials_lookup(account):
    '''
    To check if there are credentials for an account name and returns true of false based on the outcome
    '''
    return Credentials.credentials_existance(account)

def password_generate():
    '''
    To generate a random password for a user
    '''  
    autogen_pass = Credentials.passwordGenerator()
    return autogen_pass

def password_copy(account):
    '''
    Using pyperclip, it will copy the password of the specified account
    '''
    return Credentials.copy_password(account)

def password_locker():
    print("Hello and Welcome to you one stop Account store... \n Kindly key in one of the following to proceed.\n CA --- To create a new account \n LI --- LIst existing account  \n")
    user_reply = input('').lower().strip()
    if user_reply == 'ca':
        print('Sign Up')
        print ('*' * 40)
        username = input('UserName: ')
        while True:
            print('Key in TP - To type in your own password:\n GP - For a randomly generated password')
            password_choice = input().lower().strip()
            if password_choice == 'tp':
                password1 = input('Enter Your Password\n')
                passwordre = input('Kindly enter your password again\n')
                if password1 == passwordre:
                    password = password1
                    break
                else:
                    print('*' * 40)
                    print('Your Passwords do not match. Kindly try again')
                    print('*' * 40)                
            elif password_choice == 'gp':
                password = password_generate()
                break
            else:
                print('Invalid password Choice. Kindly Try again')
        new_user_creation(username, password)
        print('*' * 40)
        print(f'Hello {username}. You Account has successfully been created. You password is {password}. Cheers')
        print('*' * 40)

    elif user_reply == 'li':
        print('*' * 50)
        print('Kindly enter you Username and Password to login:')
        print('*' *50)
        username = input('User Name: ')
        password = input('Password: ')
        login = user_login(username, password)
        if user_login(username,password) == login:
            print(f'Hello {username}. Welcome to your Password Store Manager\n')

            while True:
                print('Kindly key in one of short codes for you choice:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n')
                code_choice = input().lower().strip()
                if code_choice == 'cc':
                    print('Create New Credentials')
                    print('*' * 25)
                    print('What is the account name ....')
                    account = input().lower()
                    print('What is your account username')
                    username = input()
                    while True:
                        print('For your password kindly key in any of the choices below')
                        print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                        password_choice = input().lower().strip()
                        if password_choice == 'tp':
                            password = input('Enter Your Preferred Password:\n')
                            break
                        elif password_choice == 'gp':
                            password = password_generate()
                            break
                        else:
                            print('Invalid Password option. Kindly Try again!!')
                    save_new_credentials(account,username,password)
        
                elif code_choice == 'dc':
                    if account_details_display():
                        print('Here is a list of your Accounts: ')
                        print('*' *40)
                        for account in account_details_display():
                            print(f'Account: {account.account} \n User Name: {username} \n Password: {password}')
                            print('*' *40)
                    else:
                        print('You do not have any credentials saved yet!!!')
                elif code_choice == 'fc':
                    print('Enter the name of tha Account you are looking for: ')
                    accName_search = input().lower()
                    if credentials_lookup(accName_search):
                        search_credentials = credentials_lookup(accName_search)
                        print(f"Account Name: {search_credentials.account}")
                        print('_' * 40)
                        print(f'User Name: {search_credentials.username} Password : {search_credentials.password}')
                        print('_' * 40)
                    else:
                        print('The credentials for the Account you provided do not exist!!!')
                elif code_choice == 'd':
                    print('Enter the name of the account you want to delete')
                    search_account = input().lower()
                    if credentials_lookup(search_account):
                        search_credentials = credentials_lookup(search_account)
                        print('*' * 40)
                        search_credentials.credentials_delete()
                        print('*' * 40)
                        print(f'Your account credentials for the account: {search_credentials.account} have sucessfully been deleted')
                        print('*' * 40)
                    else:
                        print("The credentials you wish to delete do not exist in the store")
                elif code_choice == 'gp':
                    password = password_generate()
                    print(f'{password} has been generated successfully. You can now copy and use it in your account')
                elif code_choice == 'ex':
                    print('Thank you for trusting us with your accounts and passwords. See you next time')
                    break
                else:
                    print('Wrong short codes keyed in. Kindly check from the options provided and try again')
    else:
        print('Kindly provode a valid input to proceed')


if __name__ == '__main__':
    password_locker()