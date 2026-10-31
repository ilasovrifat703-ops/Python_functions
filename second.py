def factorials(n : int):
    '''

    :param n: число, до которого будем искать факториал чисел
    :return: последовательный вывод вычисленного факториала для каждого числа
    '''

    if n == 1:
        return 1

    elif n > 1:
        return factorials(n-1) * n

