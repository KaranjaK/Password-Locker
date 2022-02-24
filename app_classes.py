import string
import pyperclip
import random

class User:
    '''
    This will create a Users class whereby a new instance of user will be generated.
    '''
    user_list = []

    def __init__(self, username, password):
        '''
        Initial method that will define the user properties
        '''
        self.username = username
        self.password = password
    
    def new_user(self):
        '''
        This method will initialize the creation of a new user into the user list
        '''
        User.user_list.append(self)

    
    @classmethod
    def user_display(cls):
        '''
        method displays the user account details
        '''
        return cls.user_list
    
    def user_delete(self):
        '''
        method will be used to delete a user accout from the list
        '''
        User.user_list.remove(self)

class Credentials():
        '''
        Credentials class will facilitate the creation of new Credential objects
        '''
        credentials_list = []
        
        @classmethod
        def user_verification(cls,username, password):
            '''
            method verifies if user is registered in our list
            '''

            user_this = ''
            for user in User.user_list:
                if(user.username == username and user.password == password):
                    user_this == user.username
            return user_this

        def __init__(self, username, password, account):
            '''
            method to define the creditials of a user that have to be stored
            '''
            self.username = username
            self.password = password
            self.account = account

        def store_details(self,account, username, password):
            ''''
            method to store user's credentials in the list of credentials 
            '''
            self.username = username
            self.password = password
            self.account = account
            Credentials.credentials_list.append(self)

        def delete_details(self):
            '''
            method to delete credentials from the credentials list
            ''' 
            Credentials.credentials_list.remove(self)

        @classmethod
        def credentials_search(cls, account):
            '''
            Method will pick the name of the account provided, search through the credentials and return an matches
            '''
            for credential in cls.credentials_list:
                if credential.account == account:
                    return credential

        @classmethod
        def copy_password(cls, account):
            credetials_found = Credentials.credentials_search(account)
            pyperclip.copy(credetials_found.password)

        @classmethod
        def credentials_existance(cls, account):
            '''
            Method will check if a credential exists and return true or false based on the findings
            '''
            for credential in cls.credentials_list:
                if credential.account == account:
                    return True
            return False
        
        @classmethod
        def show_credentials(cls):
            '''
            Method will show all the credentials in the credentilas list
            '''
            return cls.credentials_list

        def passwordGenerator (stringlength=10):
            ''''
            Method will generate a random password consisting of letters, numbers and special characters
            '''
            password = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*&^%$#@!~'
            return ''.join(random.choice(password) for i in range(stringlength))