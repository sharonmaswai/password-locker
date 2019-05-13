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

def main():
    print("Hello!!\n Welcome.")
    print("\n")
    name=input("What is your name?")
    username=input("Create your username:")
    password=input("Now create your unique password:")
    print(f " Welcome {username! Please select the next step.")

    while True:
        save_credentials(create_new_credentials(platform,username,password))

        print("Select any of the following short codes:1- Create a new account, 2-Find a user, 3- Exit" )
        if short_code == '1':
           print("New account")
           platform = input("Enter platform i.e facebook, instagram, twitter etc:")

           print("Usename:")
           username = input()

           print("Password:")
           password = input()

           save_credentials(create_account(username,password))
           print('\n')
           print(f "Your {platform} credential have been received and saved.")

        elif short_code =='2':
           print("Enter the username of the account you wish to find:")

           search_username = input()
           if find_user_by_name(search_user):
              search_user = find_username(search_username)
              print(f "{search_user.platform} {search_user.username")

              print(f "Password...{search_user.password}")

           else:
            print("The user does not exist.")

        elif short_code=='3':
            print(f "Goodbye, {username}")


if __name__ == '__main__':
  main()
