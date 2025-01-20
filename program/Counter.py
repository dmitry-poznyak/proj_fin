from JsonFile import JsonFile

class Counter:
    def __init__(self):
        self.file = JsonFile('animals.json')
        self.animals_amount = len(self.file.readAll())
    def add(self):
        self.animals_amount += 1
    def remove(self):
        self.animals_amount -= 1