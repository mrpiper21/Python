print('''
1. Login
2. Create an account''')

db = {}

try:
    with open('data_base.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split()
            db[username] = password
except FileNotFoundError:
    open('data_base.txt', 'w').close()

uu = int(input('Enter a number: '))

if uu == 1:
    attempts = 2
    while attempts > 0:
        username = input('Username: ')
        password = input('Password: ')
        if username in db and db[username] == password:
            print('Logged in Successfully!')
            break
        else:
            print('Incorrect username or password')
            attempts -= 1

if uu == 2:
    first_name = input('Enter your First name: ')
    last_name = input('Enter your Last name: ')
    username = input('Create a username: ')
    password = input('Create a password: ')

    while len(password) < 7:
        print('Create a strong password with at least 7 characters')
        password = input('Create a password: ')

    db[username] = password

    with open('data_base.txt', 'a') as file:
        file.write(f'{username}\n{password}\n')