from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
counter = 0
numbers = []

while counter < 10:
    val = int(input('Enter the value: '))
    numbers.append(val)
    if val > num:
        print(f'Your number is greater than the specified one')
    elif val < num:
        print(f'Your number is less than the specified one')
    elif val == num:
        print(f'Congratulations!')
        break
    print(f'List of entered numbers: {numbers}')
    counter += 1
if counter == 10:
    print("You are so bad!")