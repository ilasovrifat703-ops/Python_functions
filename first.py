string = input()

def remove_alphs(data):
    s = ''
    for i in data:
        if i in '(){}[]':
            s+=i
    return s

def f(s,summ_1,summ_2,summ_3,old_str = '') -> str:
    s = remove_alphs(s)
    if s[0] == '(':
        summ_1 += 1
    elif s[0] == '{':
        summ_2 += 1
    elif s[0] == '[':
        summ_3 += 1

    elif s[0] == ')':
        summ_1 -= 1
    elif s[0] == '}':
        summ_2 -=1
    elif s[0] == ']':
        summ_3 -= 1

    old_str+=s[0]
    if summ_3 == -1 or summ_2 == -1 or summ_1 == -1:
        return False

    if len(s) == 1 and s in ')]}':
        return True

    if len(s) == 1 and s not in ')]}':
        return False

    return f(s[1:],summ_1,summ_2,summ_3)


print(f(string,0,0,0))