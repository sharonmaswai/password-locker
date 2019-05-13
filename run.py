from user import User
from user import Credentials


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
    new_user_credentials=Credentials(platforrm,username,password)

def save_credentials():
    '''
    Function that saves the created credentials.
    '''

    Credentials.save_credentials()

def main():
    user_name=input("Hello! Welcome to Password locker.\n Tell us your name. ")
    print("Hello {}, what do you want to do?".format(user_name))






    while True:


        short_code=input("Select any of the following short codes: \n ca- Create a new account \n fu-Find a user \n x- Exit:" )



        if short_code == "ca":


           print("New account")
           platform = input("Enter platform i.e facebook, instagram, twitter etc:")

           print("Username:")
           username = input()

           print("Enter your password:")
           password= input()

           save_response=input("Would you like to save your account credentials?: y/n \n")
           if save_response=="y":
               
               print ("Welcome {}, you have successfully created a {} account: \n Here are your credentials: {} \n {}".format(username,platform, username,password))

        elif short_code =='fu':
           print("Enter the username of the account you wish to find:")

           search_username = input()
           if find_user_by_name(search_user):
              search_user = find_username(search_username)
              print("{} {}".format(search_user.platform,search_user.username))

              print( "Password:{}".format(search_user))

           else:
            print("The user does not exist.")

        elif short_code=='x':
            print("Goodbye, {}".format(user_name))


if __name__ == '__main__':
  main()
