a, b, c = 2, 2, 3
sqrt = (b ** 2 - 4 * a * c) ** 0.5
x1, x2 = (-b + sqrt) / (2 * a), (-b - sqrt) / (2 * a)
print(f'{x1=}, {x2=}')