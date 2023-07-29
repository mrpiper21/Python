class person:
    number0fclass = 0
    def __init__(self, name, age, height): #constructor
        self.name = name
        self.age = age
        self.height = height
        person.number0fclass += 1

    def __del__(self):
        person.number0fclass -= 1

    def __str__(self):
        return('Name: (), Age: (), Height: ()'.format(self.name, self.age, self.height))

    def get_older(self):
        year = 0
        self.age += year
    #Class variables



person1 = person("Comrade", 22, 182)
person2 = person("Anita", 16, 160)
person3 = person('Jonnathan', 33, 176)
print(person1)
# print(person1.age)
# print(person1.height)
print(person2.name)
print(person.number0fclass)
#Defining a dstructor
del person1
