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

    if '()' in string:
        return check_brackets(string.replace('()','',1))
    if "[]" in string:
        return check_brackets(string.replace("[]", "", 1))
    if "{}" in string:
        return check_brackets(string.replace("{}", "", 1))

    return 'Неправильно'

print(f'Скобки расставлены {check_brackets(only_brackets_str)}')


