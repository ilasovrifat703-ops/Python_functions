from re import findall


string = input('Введите строку: ')

def find_abbrs(text):

    path = r'\b[A-ZА-Я]{2,6}\b'
    result = findall(path,text)

    return result

result_abbrs = find_abbrs(string)

for abbr in result_abbrs:
    print(abbr)
