class person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return('name: (), age: (), height: ()'.format(self.name, self.age, self.height))

class player(person):
    def __init__(self, name, age, height, teamsPlayed):
        super(player, self).__init__(name, age, height)
        self.teamsPlayed = teamsPlayed
    def teams(self):
        return self.teamsPlayed
x = player('luffy', 34, 1.23, 12)
print(x.name)