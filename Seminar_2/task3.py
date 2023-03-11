a = 10


def get_number(value: int, base: int):
    result = ''
    while value > 0:
        result = str(value % base) + result
        value //= base

    return result


print(oct(9))
print(get_number(9, 8))