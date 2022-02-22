from curses.ascii import CR
from hashlib import new
from app_classes import User
from app_classes import Credentials

def new_user_crearion(username, password):
    '''
    To create a new user with a suer name and password
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

def save_new_credentials():
    '''
    To save new credentials to the credentials list
    '''
    Credentials.store_details()

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

    