def fizz_buzz():
    for i in range(1, 100 + 1):
        if i % 15 == 0:
            yield 'fizz_buzz'
        elif i % 3 == 0:
            yield 'fizz'
        elif i % 5 == 0:
            yield 'buzz'
        else:
            yield i


print(*fizz_buzz())

