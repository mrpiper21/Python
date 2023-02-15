print('''
1. Login
2. Create an account''')
lop = list()
db = open('data_base.txt', 'a')
uu = int(input('Enter a number: '))
dd = open('data_base.txt', 'r')
if uu == 1:
    attempts = 2
    for l in dd:
        while True:
            un = input('user name: ')
            up = input('password: ')
            if un != l or up == l:
                print('Incorrect password*')
                atttempts = attempts - 1
                print(attempts)
                if attempts == 0:
                    break
            if un == l or up != l:
                 print('Incorrect User name')
                 attempts = attempts - 1
                 print(attempts)
                 if attempts == 0:
                    break
            else:
                 print('Logged in Successful!')
            break

if uu == 2:
     fn = input('Enter your First name: ')
     ln = input('Enter your last name: ')
     cun = input('Create a user name: ')
     cup = input('Create a password: ')
     if len(cup) < 7:
         print('Create a strong password with at least 7 charcters')
     pass
     #print('Enter a strong password!')
     db.write((cun + '\n' + cup + '\n'))
     
     