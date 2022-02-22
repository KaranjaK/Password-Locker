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

        def store_details(self):
            ''''
            method to store user's credentials in the list of credentials 
            '''
            Credentials.credentials_list.append(self)

        def delete_details(self):
            '''
            method to delete credentials from the credentials list
            ''' 
            Credentials.credentials_list.remove(self)

            