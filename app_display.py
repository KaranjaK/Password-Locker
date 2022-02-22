from hashlib import new
from app_classes import User
from app_classes import Credentials

def new_user_crearion(username, password):
    '''
    To create a new user with a suer name and password
    '''
    new_user = User(username, password)
    return new_user
