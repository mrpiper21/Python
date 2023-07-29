def append_database(Username, Userpassword):
    # Stores the username and user-password in the database
    USER_BASE = open('sensitiveinfo.txt', 'a')
    USER_BASE.write(Username + ': ' + Userpassword + 'n')
    USER_BASE.close()  # Close userbase after storage

def read_database(username, userpassword):
    # Read through database and check whether username and user-password are in the database
    USER_BASE = open('sensitiveinfo.txt', 'r')
    for line in USER_BASE:
        if line.startswith(username):
            password = findpassword(line)
            if userpassword == password:
                return 1
        else:
            return 0

def findpassword(passvalue):
    delimeter = ':'
    passvalue = passvalue.rstrip('n')
    string_valueP = passvalue[passvalue.index(delimeter) + 1:]
    string_valueP = string_valueP.replace(" ", "")
    return string_valueP

print('''
1. Login
2. Create an account''')
prompt = 0
for i in range(3):
    try:
        num = int(input('Enter a number: '))  # Prompt user whether to login or to create an account
        if num == 1 or num == 2:
            prompt = num
            break
        else:
            print('Enter 1 or 2 to proceed')
            pass
    except:
        print("value must be a digit")

def login(PROMPT):  # Ask user to login
    if PROMPT == 1:
        for i in range(5):
            user_name = input("User name: ")
            user_pass = input("User password: ")
            approval = read_database(user_name, user_pass)
            if i == 4:
                print("Attempts exhausted, try again in an hour time")
                break
            if approval == 1:
                print("Loggin successful!")
                break
            else:
                print("invalid username or password")
                pass

login(prompt)

def create_account(PROMPT):  # Ask user to create account
    if PROMPT == 2:
        first_name = input('Enter your First name: ')
        last_name = input('Enter your last name: ')
        USER_NAME = input('Create a user name: ')
        for i in range(5):
            USER_PASS = input('Create a password: ')
            for i in USER_PASS:
                if ord(i) >= 65 and ord(i) <= 95 or ord(i) >= 97 and ord(i) <= 122:
                    break
                elif ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 32 and ord(i) <= 152:
                    break
                else:
                    print("Password must include uppercase letter, lowercase letter and a digit!")
                    pass
                if len(USER_PASS) < 7:
                    print('Create a strong password with at least 7 charcters')
                    pass
                else:
                    if len(USER_PASS) > 7:
                        append_database(USER_NAME, USER_PASS)
                        print("Account created!")
                        break

create_account(prompt)