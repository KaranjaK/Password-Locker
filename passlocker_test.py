from cgi import test
import unittest
from app_classes import User
from app_classes import Credentials

class UsersTest (unittest.TestCase):
    '''
    Class that will define the various tests for the user class 
    '''
    def default_user(self):
        '''
        Very first test before any other user methods test runs
        '''

        self.new_user = User('KaranjaK','K74@yea')

    def initialization_test(self):
        ''''
        Proper Initialization test
        '''
        self.assertEqual(self.new_user.username,'KaranjaK')
        self.assertEqual(self.new_user.password, 'K74@yea')

    def userSave_test(self):
        '''
        To test if a new user has been added successfully in the list
        '''
        self.new_user.new_user()
        self.assertEqual(len(User.user_list),1)

class CredentialsTest(unittest.TestCase):
    '''
    Class that defines various test cases for the credentials class
    '''
    def user(self):
        '''
        Very first test to test if individual test methods run
        '''
        self.newSet_credentials = Credentials('KaranjaK','K74@yea', 'Email')
    
    def initialize_test(self):
        '''
        To check if the Credentials have been initialized correctly
        '''
        self.assertEqual(self.newSet_credentials.username, 'KaranjaK')
        self.assertEqual(self.newSet_credentials.password, 'K74@yea')
        self.assertEqual(self.newSet_credentials.account, 'Email')
    
    def store_credentials_test(self):
        '''
        To check if the credentials have been saved into the credentials list
        '''
        self.newSet_credentials.store_details()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def cleanUp(self):
        '''
        To clean up after every test case has been run
        '''
        Credentials.credentials_list = []

    def multiple_account_storing(self):
        '''
        To check on possiblity of saving multiple credentials on the credentials list
        '''
        self.newSet_credentials.store_details()
        test_credential = Credentials ('UleMsee', 'H789kfg', 'Instagram')
        test_credential.store_details()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def credentials_delete_test(self):
        '''
        To check posibility of removing credentials from the list
        '''
        self.newSet_credentials.store_details()
        test_credential = Credentials ('UleMsee', 'H789kfg', 'Instagram')
        test_credential.store_details()
        self.newSet_credentials.delete_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def search_credentials_test(self):
        '''
        To check possibility of find and displaying credentials
        ''' 

        self.newSet_credentials.store_details()
        test_credential = Credentials ('UleMsee', 'H789kfg', 'Instagram')
        test_credential.store_details()
        search_credential = Credentials.credentials_search('Instagram')
        self.assertEqual(search_credential.account, test_credential.account)

    def existance_credentials_test(self):
        '''
        To check possibility of getting a false of true reply based on a credential existing or not
        '''
        self.newSet_credentials.store_details()
        test_credential = Credentials ('UleMsee', 'H789kfg', 'Instagram')
        test_credential.store_details()
        if_credential_found = Credentials.credentials_existance('Instagram')
        self.assertTrue(if_credential_found)