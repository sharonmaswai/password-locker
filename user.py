import pyperclip
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



class Credentials:
  '''
  Class that generates new instances of user credentials of the application
  '''
  user_credentials= [] #an empty list

  def __init__(self,platform,username,password):

    self.platform = name
    self.username = username
    self.password = password
