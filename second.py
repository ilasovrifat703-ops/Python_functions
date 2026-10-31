def fib_nums(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fib_nums(n-1) + fib_nums(n-2)

for i in range(1,20):
    print(fib_nums(i))