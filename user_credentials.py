import random
import pyperclip
import string

class User:
    """
    creat pwd locker accounts and save 
    """
    users=[]
    def __init__(self,firstname,lastname,password):
        """
        function to define properties for user object
        """
        self.firstname=firstname
        self.lastname=lastname
        self.password=password
        
        
    def save_user(self):
        """
        function to save user information
        """    
        User.users.append(self)
        
        
class Credential:
    """
    create creadentials account and save also generate passwords
    """
    credentials=[]
    @classmethod 
    def confirm_user(self,firstname,password): #cls meaning
        """
       function to confirm wheather names and password entered match
        """
        current_user=""
        for user in User.users:
            if (user.firstname==firstname and user.password==password):
                current_user=user.firstname
                
        return current_user
    
    
    def __init__(self,username,sitename,accountname,password):
        
        """
        function to create credential and define their properties
        """
        self.username=username
        self.sitename=sitename
        self.accountname=accountname
        self.password=password
        
    def save_credentials(self):
        """
        function to save user information 
        """ 
        Credential.credentials.append(self)   
     
     
    def generate_password(size=8,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        generate  password using letters and numbers.
        '''
        gen_pass=''.join(random.choice(char)for _ in range(size))
        return gen_pass
    
    @classmethod   
    def show_credentials(cls,username): 
        """
        function to show available user credentials 
        """
        credentials_saved=[]
        for credential in cls.credentials:
            if credential.username==username:
               credentials_saved.append(credential)
        return credentials_saved
    
    @classmethod
    def find_site_by_name(cls,sitename):
        '''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
        for credential in cls.credentials:
            if credential.sitename ==sitename:
                return credential
            
            
		
    @classmethod
    def copy_credentials(cls,sitename):
        """
        copy credentials
        """
        find_credential=Credential.find_site_by_name(sitename)
        return pyperclip.copy(find_credential.password)                                
    
    
    
#     def delete(self,sitename):       
#        """
#        function to delete pwd locker account  
#        """
#        #write function to delete