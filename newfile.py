#Creating a simple user loggins

print('''
1. Login
2. Create an account''')

uu = int(input('Enter a number: '))
if uu == 1:
    data_base = open('data_base.txt', 'r')
    Av_database = data_base.read()
    for i in range(3):
        username = input("Enter username: ")
        usercode = input("Enter password: ")
        #print(i)
        if username in Av_database and usercode not in Av_database:
            print("Incorrect password*")
            pass
        if username not in Av_database and usercode in Av_database:
            print("Incorrect username*")
            pass
        if username in Av_database and usercode in Av_database:
            print("Logging Successful!")
            if usercode == username:
                print("Incorrect password!")
                pass
            break
        if i == 2:
            print("You have been denied access!")

if uu == 2:
     fn = input('Enter your First name: ')
     ln = input('Enter your last name: ')
     cun = input('Create a user name: ')
     cup = input('Create a password: ')
     print("Account created!")
     if len(cup) < 7:
         print('Create a strong password with at least 7 charcters')
     pass
     dd = open('data_base.txt', 'a')
     dd.write(cun + "\n")
     dd.write(cup + "\n")
     dd.close()

     
     