from user import User
from user import credentials
import sys

def create_account(username,password):
    new_user_account=User(username,password)
    return new_user_account


def save_users_credentials(user):
  '''
  This is a function that saves the user's credentials
  '''
  user.save_credentials()

def find_user_by_name(username):
  '''
  This function finds a user using the username they entered
  '''
  return User.find_user_by_name(username)

def  confirm_user(username):
    '''
    validates a user's account by checking the existence of username
    '''
    return user_account_exists(name)
def show_user():

    return User.show_user()

def create_new_credentials(platform,username,password):
    '''
    This function creates a new locked accounts
    '''
    new_user_credentials=Credentials(platform,username,password)

def save_credentials():
    '''
    Function that saves the created credentials.
    '''

    Credentials.save_credentials()
