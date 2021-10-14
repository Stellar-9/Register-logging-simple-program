import IdentityService

username = input("Enter username: ")
while True:
    password = input("Enter password: ")
    password_confirm = input("Confirm password: ")
    if password == password_confirm:
        print("Registration was successfull")
        break
    else:
        print("Passwords are not matching. Please enter password again")

test = IdentityService.IdentityService()
test.register(username, password)
test.save_to_json('./credentials.json')

