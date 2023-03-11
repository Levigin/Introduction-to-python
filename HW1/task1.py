
while True:
    a = int(input('Enter the side a: '))
    b = int(input('Enter the side b: '))
    c = int(input('Enter the side c: '))
    if a + b < c or a + c < b or b + c < a:
        print(f'There is no triangle with such sides!')
    elif a != b != c:
        print(f'The triangle is versatile')
    elif a == b == c:
        print(f'The triangle is equilateral')
    elif a == b or a == c or b == c:
        print(f'The triangle is isosceles')

    exit_ = input('To exit, enter "exit" or any letter otherwise, enter "continue": ')
    if exit_ == 'continue':
        continue
    else:
        break
