# import pyperclip
from user_credentials import User, Credential

def create_user(firstname,lastname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(firstname,lastname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def confirm_user(firstname,password):
	'''
	verifies the user before creating credentials
	'''
	confirm_user = Credential.confirm_user(firstname,password)
	return confirm_user

def generate_password():
	'''
	generate a password automatically
	'''
	gen_pass =Credential.generate_password()
	return gen_pass

def create_credential(username,sitename,accountname,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(username,sitename,accountname,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def show_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.show_credentials(user_name)
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credentials(site_name)

def main():
	print(' ')
	print("Hello! Welcome to Password Locker.")
	while True:
		print(' ')
		print("-"*60)
		print("Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit")
		short_code = input("Enter a choice: ").lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print("To create a new account:")
			first_name = input("Enter your first name - ").strip()
			last_name = input("Enter your last name - ").strip()
			password = input("Enter your password - ").strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f"New Account Created for: {first_name} {last_name} using password: {password}")
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print("To login, enter your account details:")
			user_name = input("Enter your first name - ").strip()
			password = str(input("Enter your password - "))
			user_exists = confirm_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f"Welcome {user_name}. Please choose an option to continue.")
				print(' ')
				while True:
					print("-"*60)
					print("Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit")
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print("Enter your credential details:")
						site_name = input("Enter site\'s name- ").strip()
						account_name = input("Enter account\'s name - ").strip()
						while True:
							print(' ')
							print("-"*60)
							print("Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit")
							psw_choice = input("Enter an option: ").lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input("Enter password: ").strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print(" Wrong option entered. Try again.")
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f"Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}")
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if show_credentials(user_name):
							print("Here are your credentials")
							print(' ')
							for credential in show_credentials(user_name):
								print(f"Site Name: {credential.sitename} - Account Name: {credential.accountname} - Password: {credential.password}")
							print(' ')	
						else:
							print(' ')
							print("You don't have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input("Enter site name for credential password to copy: ")
						copy_credential(chosen_site)
						print('')
					else:
						print(" Wrong option entered. Try again.")

			else: 
				print(' ')
				print(" Wrong details entered. Try again or Create an Account.")		
		
		else:
			print("-"*60)
			print(' ')
			print("Wrong option entered. Try again.")
				






if __name__ == '__main__':
	main()

