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
         self.assertEqual(self.new_user.username,"Sharon")
         self.assertEqual(self.new_user.password,"mas7000")

if __name__ == '__main__':
    unittest.main()
