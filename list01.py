x = [3, 3, 6, 7, 3 , 54]

def square(num):
    return num * num

y = [square(i) for i in x]
print(y)