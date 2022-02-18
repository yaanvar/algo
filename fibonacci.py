def fib(n):
    f1, f2 = 0, 1
    while n:
        n -= 1
        f1, f2 = f2, f1 + f2
    return f1

#main
n = int(input())
print(fib(n))