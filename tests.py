import unittest
from user_credentials import User,Credential
import pyperclip

class TestUser(unittest.TestCase):
    """
    test class defining cases for the user class behaviuor
    """
    
    def setUp(self):
        """
        function to create  account before test
        """
        
        self.newuser=User('Christine','Ombima','tyna452')
    
    def test__init__(self):
        """
        Test to check if account creation was done correctly
  		"""
        self.assertEqual(self.newuser.firstname,'Christine')
        self.assertEqual(self.newuser.lastname,'Ombima')
        self.assertEqual(self.newuser.password,'tyna452')
  
    def test_save(self):
      """
      test to check if new user info is saved
      """
      self.newuser.save_user()
      self.assertEqual(len(User.users),1)
      
      
      
class TestCredentials (unittest.TestCase):   
    """
    test class defining cases for the credentials class behaviuor
    """ 
    def confirm_user(self):
      """
      function to confirm 
      """
        
      self.newuser = User("Christine","Ombima","tyna452")
      self.newuser.save_user()
      user2=User("alex","nad","nad452")
      user2.save_user()
      
      for user in User.users:
          if user.firstname==user2.firstname and user.password==user2.password:
              current_user=user.firstname
      return current_user
      
    #   self.assertEqual(current_user,Credential.confirm_user(user2.firstname,user2.password)) 
      
#     def setUp(self):
#       """
#       function to create create credentials before test
#       """ 
#       self.new_credential=Credential("Christine","Facebook","chrisombima","tyna452") 
      
#     def test__init__(self):
#         """
#         test to check if credential were created correctly
#         """      
#         self.assertEqual(self.new_credential.username,"Christine")
#         self.assertEqual(self.new_credential.sitename,"Facebook")
#         self.assertEqual(self.new_credential.accountname,"chrisombima")
#         self.assertEqual(self.new_credential.password,"tyna452")
        
#     def test_save_credentials(self):
#         """
#         test to check if new credentials info has been saved
#         """ 
#         self.new_credential.save_credentials()
#         twitter= Credential("alex","Twitter","nad","nad452") 
#         twitter.save_credentials()
#         self.assertEqual(len(Credential.credentials),4)
        
    
#     def test_copy_credential(self):
#         """
#         test to confirm credential method copies correctly
#         """
#         self.new_credential.save_credentials()
#         twitter=Credential("alex","Twitter","nad","nad254")
#         twitter.save_credentials()
#         find_credential=None
#         for credential in Credential.credentials:
#             find_credential=Credential.find_site_by_name(credential.sitename)
#             return pyperclip.copy(find_credential.password)
#         Credential.copy_credentials(self.new_credential.sitename)
#         self.assertEqual("tyna452",pyperclip.paste())
#         print(pyperclip.paste())
        

# if __name__ == '__main__':
# 	unittest.main()