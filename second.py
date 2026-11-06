number = int(input('Введите число: '))

def find_fib(n : int) -> int:
    '''
    Поиск запрошенного ряда Фибоначчи
    :param n: номер запрошенного ряда Фибоначчи
    :return: вывод заропшенный элемент ряда Фибоначчи
    '''

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return (find_fib(n-1) + find_fib(n-2))

result = find_fib(number)

print(f'Полученное число: {result}')
