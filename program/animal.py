class Animal:
    def __init__(self, name, birth_date, commands):
        self.name = name
        self.birth_date = birth_date
        self.commands = commands

class HomeAnimal:
    def __init__(self, name, birth_date, commands):
        super(HomeAnimal, self).__init__(name, birth_date, commands)

class PackAnimal:
    def __init__(self, name, birth_date, commands):
        super(PackAnimal, self).__init__(name, birth_date, commands)