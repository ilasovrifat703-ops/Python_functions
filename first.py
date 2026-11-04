string = input('Введите строку: ')

only_brackets_str = ''
for ch in string:
    if ch in '()[]{}':
        only_brackets_str+=ch

def check_brackets(string):
    if not(string):
        return True

    if '()' in string:
        return check_brackets(string.replace('()','',1))
    elif "[]" in string:
        return check_brackets(string.replace("[]", "", 1))
    elif "{}" in string:
        return check_brackets(string.replace("{}", "", 1))

    return False

print(check_brackets(only_brackets_str))


