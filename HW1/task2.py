
flag = False
val = input('Enter the value: ')
if '-' in val:
    print(f'Invalid data')
elif int(val) > 100_000:
    print(f'Invalid data')
else:
    val = int(val)
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            flag = True
            print(f'Number is a composite')
            break
    if not flag:
        print(f'Number is a prime')
