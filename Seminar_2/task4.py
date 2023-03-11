import math
import decimal

decimal.getcontext().prec = 42


def get_square_or_len_circle(r):
    square_circle = decimal.Decimal(math.pi * r ** 2)
    len_circle = decimal.Decimal(2 * math.pi * r)
    return f'square_circle: {square_circle}, len_circle: {len_circle}'


print(get_square_or_len_circle(10))