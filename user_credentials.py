

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
        
        
#     def save_user(self):
#         """
#         function to save user information
#         """    
#         User.users.append(self)
        
        
# class Credential:
#     """
#     create creadentials account and save also generate passwords
#     """
#     credentials=[]
#     #something 
#     def confirm_user(self,firstname,lastname,password): #cls meaning
#         """
#        function to confirm wheather names and password entered match
#         """
#         current_user=""
#         for user in User.users:
#             if (user.firstname==firstname,user.lastname==lastname and user.password==password):
#                 current_user=user.firstname+user.lastname
                
#         return current_user
    
    
#     def __init__(self,username,sitename,accountname,password):
        
#         """
#         define properties for user object
#         """
#         self.username=username
#         self.sitename=sitename
#         self.accountname=accountname
#         self.password=password
        
#     def save_credentials(self):
#         """
#         function to save user information 
#         """ 
#         #credentials=[]
#         Credential.credentials.append(self)   
     
     
#     def generate_password(self,size=8): 
#         """
#         function to generete password
#         """
#          #write function to genereate password
     
#     def show_credentials(self,username): #cls meaning
#         """
#         function to show available user credentials 
#         """
#         credentials_saved=[]
#         for credential in self.credentials:
#             if credential.username==username:
#                 credentials_saved.append(credential)
#         return credentials_saved
    
#     def delete(self,sitename):       
#        """
#        function to delete pwd locker account  
#        """
#        #write function to delete