number = int(input('Введите число: '))

def find_fact(num):
    '''
    Нахождение факториала числа num
    :param num: число, факториал которого ищем
    :return: факториал числа num
    '''

    if num == 1:
        return 1

    else:
        return find_fact(num-1) * num

for num in range(1,number+1):
    result = find_fact(num)

    print(num,'',result)
