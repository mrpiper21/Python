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

    # def get_older(year):
    #     return self.age += year

#inheritance
class worker(person):
    def __init__(self, name, age, height, salary):
        super(worker, self).__init__(name, age, height)
        self.salary = salary
    def cal_salary(self):
        return self.salary * 12

worker1 = worker('Janet', 24, 1.67, 2000)
print(worker1)
print(worker.cal_salary(worker1))
