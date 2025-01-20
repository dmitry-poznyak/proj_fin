from NotNullInput import NotNullInput, DateInput
from JsonFile import JsonFile
from Counter import Counter

def add_animal():
    name = NotNullInput('Enter name: ').capitalize()
    birth_date = DateInput('Enter birth date: ')
    # Команды храним в виде списка
    commands = input('Enter commands that the animal can do (comma separated): ').split(',')
    commands = [command.strip() for command in commands]  # Убираем пробелы вокруг команд
    animal_type = NotNullInput('Enter animal\'s type (example: cat): ')
    animal_kind = 'unknown'

    if animal_type.upper() in ('CAT', 'DOG', 'HAMSTER'): animal_kind = 'Home animal'
    elif animal_type.upper() in ('HORSE', 'CAMEL', 'DONKEY'): animal_kind = 'Pack animal'

    # Читаем ID из файла и увеличиваем его
    try:
        with open('id', 'r', encoding='utf-8') as f:
            id = int(f.read())
    except FileNotFoundError:
        id = 1  # Если файл не найден, начинаем с 1

    animal_data = {'name': name, 'birth_date': birth_date, 'commands': commands, 'animal_kind': animal_kind, 'animal_type': animal_type}
    JsonFile('animals.json').writeValue(str(id), animal_data)

    # Обновляем ID
    with open('id', 'w', encoding='utf-8') as f:
        f.write(str(id + 1))

    Counter().add()
    print(f'Animal\'s ID is {id}')

def new_command():
    try:
        id = NotNullInput('Enter ID: ')
        command = NotNullInput('Enter new command: ')
        file = JsonFile('animals.json')
        animal = file.readValue(id)
        if animal:
            animal['commands'].append(command)
            file.writeValue(id, animal)
            print(f'Added command "{command}" to animal with ID {id}')
        else:
            print('Animal with this ID doesn\'t exist.')
    except Exception as e:
        print(f"Error adding command: {e}")

def view_commands():
    try:
        id = NotNullInput('Enter ID: ')
        animal = JsonFile('animals.json').readValue(id)
        if animal:
            print(f'Commands for {animal["name"]}: {", ".join(animal["commands"])}')
        else:
            print('Animal with this ID doesn\'t exist.')
    except Exception as e:
        print(f"Error viewing commands: {e}")

def view_animal(id = None):
    try:
        if not id: id = NotNullInput('Enter ID: ')
        animal = JsonFile('animals.json').readValue(id)
        if animal:
            print(f'ID: {id}; Name: {animal["name"]}; Birth Date: {animal["birth_date"]}; Commands: {", ".join(animal["commands"])}; Animal Kind: {animal["animal_kind"]}; Animal Type: {animal["animal_type"]}')
        else:
            print('Animal with this ID doesn\'t exist.')
    except Exception as e:
        print(f"Error viewing animal: {e}")

def remove_animal():
    try:
        id = NotNullInput('Enter ID: ')
        JsonFile('animals.json').removeValue(id)
        Counter().remove()
        print(f'Animal with ID {id} removed.')
    except Exception as e:
        print(f"Error removing animal: {e}")

def view_all():
    try:
        animals = JsonFile('animals.json').readAll()
        if animals:
            for id, animal in animals.items():
                print(f'ID: {id}; Name: {animal["name"]}; Birth Date: {animal["birth_date"]}; Commands: {", ".join(animal["commands"])}; Animal Kind: {animal["animal_kind"]}; Animal Type: {animal["animal_type"]}')
        else:
            print('There aren\'t any animals.')
    except Exception as e:
        print(f"Error viewing all animals: {e}")
