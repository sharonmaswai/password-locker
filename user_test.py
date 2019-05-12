import unittest
import sys
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
     def tearDown(self):
        User.user_info=[]

        '''
        Ensures the user_info is clean before the next method is applied
        '''

     def setUp(self):

        self.new_user = User("Sharon","mas7000")
        self.new_user_credentials = Credentials("instagram","sharonmaswai","mas7000")

     def test_if_object_is_initialized(self):
         '''
         test_if_object_is_initialized test case to test if the object has been initialized properly

         '''
         self.assertEqual(self.new_user.username,"Sharon")
         self.assertEqual(self.new_user.password,"mas7000")

     def test_for_successful_saving_of_users(self):

         '''
         Check if the the new user details have been saved
         '''

         self.new_user.save_user_info()
         self.assertEqual(len(User.user_info),1)
     def test_for_ability_to_save_credentials(self):
         '''
         Checks if a user can save their credentials by appending the credentials to the user credentials list
         '''
         self.new_user_credentials.save_credentials()
         self.assertEqual(len(Credentials.user_credentials),1)


     def test_if_user_can_login_with_existing_account(self):
         '''
         checks if a user can login with their existing account
         '''
         self.new_user.save_user_info()
         user_account_exists = User.find_user_by_name("Sharon")
         self.assertTrue(user_account_exists)


     def test_user_verification_and_login(self):

         '''
         Test if user can be verified and log into their existing account.
         '''
         self.new_user.save_user_info()
         verify_user = User.confirm_user("Sharon","mas7000")
         self.assertEqual(verify_user, self.new_user.username)



if __name__ == '__main__':
    unittest.main()
