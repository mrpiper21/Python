#Inheritance
class Register:
    def __init__(self, name: str, email: str, age: int):
        self.name: str = name
        self.email: str = email
        self.age: int = age


class Login(Register):
    def __init__(self, name, email, age):
        super().__init__(name, email, age)

Login("bbaah@gmail.com", "Bernard", 5)