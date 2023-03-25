def fib(n):
    prev_fib = 0
    fib_curr = 1
    for _ in range(n):
        yield prev_fib
        fib_curr = prev_fib + fib_curr
        prev_fib = fib_curr - prev_fib


list_fib = fib(9)
print(next(list_fib))
print(next(list_fib))
print(next(list_fib))
print(next(list_fib))
print(next(list_fib))
print(next(list_fib))
print(next(list_fib))
