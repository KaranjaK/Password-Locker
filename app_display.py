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

