import unittest
from app_classes import User
from app_classes import Credentials

class UsersTest (unittest.TestCase):
    '''
    Class that will define the various tests for the user class 
    '''
    def defaultUser(self):
        '''
        Very first test before any other user methods test runs
        '''

        self.new_user = User('KaranjaK','K74@yea')

    