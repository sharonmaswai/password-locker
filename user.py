import pyperclip
import sys
class User:

    '''
    A class in which new instances for accounts are added

    '''

    user_info =[]
    def __init__(self,username,password):

        self.username=username
        self.password=password

    def save_user_info(self):

        User.user_info.append(self)

    @classmethod
    def find_user_by_name(cls,username):
        '''
        Will check if value enter at the username argument exists
        '''
        for user in cls.user_info:
            if user.username == username:
                return True
            return False

    @classmethod
    def confirm_user(cls,username,password):
        '''
        checks if the username and password entered match those of an existing user
        '''
        entered_details=""
        for user in cls.user_info:
            if user.username==username and user.password==password:
                entered_details=user.username
                return entered_details




class Credentials:
  '''
  Class that generates new instances of user credentials of the application
  '''
  user_credentials= [] #an empty list

  def __init__(self,platform,username,password):

    self.platform = platform
    self.username = username
    self.password = password

  def save_credentials(self):

        self.user_credentials.append(self)

  @classmethod
  def show_credentials(cls):
        for credential in cls.user_credentials:
            return credential
