from user import User
from user import credentials

def create_account(username,password):
    new_user_account=User(username,password)
    return new_user_account
