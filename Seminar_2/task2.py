data = [1, 'hello world', 3.14, (1, 2), True]

for i, item in enumerate(data, start=1):
    print(i)
    print(id(item))
    print(item.__sizeof__())
    print(hash(item))
    if type(item) == int:
        print('integer')
    elif type(item) == str:
        print('string')

