class UserInfo:
    def __init__(self, first_name, last_name, age, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email_address = email_address

def login():
    for i in range(5):
        user_name = input("User name: ")
        user_pass = input("User password: ")
        approval = read_database(user_name, user_pass)
        if i == 4:
            print("Attempts exhausted, try again in an hour time")
            break
        if approval == 1:
            print("Login successful!")
            break
        else:
            print("invalid username or password")

def create_account():
    first_name = input('Enter your First name: ')
    last_name = input('Enter your last name: ')
    email_address = input('Enter your email address: ')
    age = int(input('Enter your age: '))
    user = UserInfo(first_name, last_name, age, email_address)
    user_name = input('Create a user name: ')

    import re
    def check_input(text):
        if (re.search(r'[A-Z]', text) and
                re.search(r'[a-z]', text) and
                re.search(r'[0-9]', text)):
            return True
        else:
            return False

    while True:
        user_pass = input('Create a password: ')
        if len(user_pass) > 7:
            if check_input(user_pass):
                append_database(user_name, user_pass)
                print("Account created!")
                break
            else:
                print("Password must contain uppercase letters, lowercase letters, and numbers. Try again.")
        else:
            print("Password must be at least 7 characters.")

def append_database(username, userpassword):
    with open('sensitiveinfo.txt', 'a') as f:
        f.write(username + ': ' + userpassword + '\n')

def read_database(username, userpassword):
    with open('sensitiveinfo.txt', 'r') as f:
        for line in f:
            if line.startswith(username):
                password = line.split(':')[1].strip()
                if userpassword == password:
                    return 1
                return 0
        return 0

print('''
1. Login
2. Create an account''')

prompt = 0

for i in range(3):
    try:
        num = int(input('Enter a number: '))
        if num == 1 or num == 2:
            prompt = num
            break
        else:
            print('Enter 1 or 2 to proceed')
    except ValueError:
        print("value must be a digit")

if prompt == 1:
    login()
elif prompt == 2:
    create_account()