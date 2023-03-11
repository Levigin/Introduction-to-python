extended_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_number(value: int, base: int):
    result = ''
    while value > 0:
        result = extended_digits[value % base] + result
        value //= base

    return result


print(hex(18))
print(get_number(18, 16))