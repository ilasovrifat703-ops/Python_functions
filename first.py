string = input('Введите строку: ')

only_brackets_str = ''
for ch in string:
    if ch in '()[]{}':
        only_brackets_str += ch

def check_brackets(string: str) -> str:
    '''
    Функция, которая проверяет корректность расстановки скобок в строке
    :param string: строка, в котором производится проверка (принимает строку только из скобок)
    :return: "Правильно", если успешно строка прошла проверку, иначе "Неправильно"
    '''

    if not(string):
        return 'Правильно'

    for pair in ['()','{}','[]']:
        if pair in string:
            new_string = string.replace(pair, '', 1)
            return check_brackets(new_string)

    return 'Неправильно'
    
result = check_brackets(only_brackets_str)

print(f'Скобки расставлены {result}')
