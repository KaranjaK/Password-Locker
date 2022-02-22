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