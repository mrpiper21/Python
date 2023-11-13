x = [3, 3, 6, 7, 3 , 54]

def square(num):
    return num * num

y = [square(i) for i in x]
print(y)

# Hihg order functions are functions that can takes in functions and list as their 
# parameters and return them as such

def my_map(func, list):
    result = []
    for item in list:
        new_item = func(item)
        result.append(new_item)
    return(result)

List = [2, 5, 2, 2, 1]
squared = my_map(lambda x: x*2, List)