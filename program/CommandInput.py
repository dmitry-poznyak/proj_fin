import Commands
import sys
from NotNullInput import NotNullInput

class CommandInput:
    def __init__(self):
        while True:
            print('Available commands:\n0 => Add new animal\n1 => View animal\'s commands\n2 => Teach animal new command\n3 => View animal\'s information\n4 => View all animals\' information\n5 => Remove animal\n6 => Exit')
            command = NotNullInput('Enter command: ')
            if command == '0':
                Commands.add_animal()
                print('Done!')
            elif command == '1':
                Commands.view_commands()
                print('Done!')
            elif command == '2':
                Commands.new_command()
                print('Done!')
            elif command == '3':
                Commands.view_animal()
                print('Done!')
            elif command == '4':
                Commands.view_all()
                print('Done!')
            elif command == '5':
                Commands.remove_animal()
                print('Done!')
            elif command == '6':
                sys.exit(0)
            else:
                print('Unknown command')