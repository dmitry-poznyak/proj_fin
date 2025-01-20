import datetime

def NotNullInput(message):
    return_=''
    while True:
        return_ = input(message)
        if return_ == '' or return_ == '\n' or return_ == None:
            print('Please enter something that\'s not empty')
            continue
        else:
            return return_

def DateInput(message):
    while True:
        return_ = input(message)
        try:
            # Преобразуем ввод в формат даты
            date = datetime.datetime.strptime(return_, "%Y/%m/%d")
            return return_
        except ValueError:
            print('Enter a valid date (ex: 2023/12/31)')
            continue
