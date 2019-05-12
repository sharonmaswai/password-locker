import unittest
import sys
from user import User

class TestUser(unittest.TestCase):
     def tearDown(self):
        User.user_info=[]
        '''
        Ensures the user_info is clean before the next method is applied
        '''

     def setUp(self):

        self.new_user = User("Sharon","mas7000")

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
         self.assertEqual(len(Users.users_list),1)



if __name__ == '__main__':
    unittest.main()
