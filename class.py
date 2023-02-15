class person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession
    def nature(self):
        print("Name:", self.name, "Sex:", self.sex, "Profession:", self.profession)
    def work(self):
        print(self.name, "is working as", self.profession)
name = input('Enter name: ')
Gender = input("Gender (M/F): ")
Prof = input("Enter profession: ")

name = person(name, Gender, Prof)
name.nature()
name.work()

class patient:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def details(self):
        print("Name:", self.name, "Age: ", self.age, "Address: ", self.address)
    def cond(self):
        print(self.name, "is", self.age, 'years old', "He/she lives at", self.address)
name = input("Patient name: ")
BY = int(input("Birth year: "))
age = 2023 - BY
ADD = input("House address: ")

name = patient(name, age, ADD)
name.details()
name.cond()
# details = dict()
# COND = dict
# details['Details'] = name.details()
# # COND['Behavior'] = name.cond()
# db = open("data_base.txt", "a")
# db.write(f'{details} \n')
# db.close()
