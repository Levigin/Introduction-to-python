def is_prime(val):
    """
    Checks a value for simplicity

    :param val: integer value
    :return: boolean value (is the prime or not)
    >>> is_prime(5)
    True
    >>> is_prime(100)
    False
    >>> is_prime(1.05)
    Traceback (most recent call last):
    ...
    TypeError: Value should be of an integer type
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: Value should be more one
    >>> is_prime(100_999)
    Traceback (most recent call last):
    ...
    ValueError: The value is too large
    >>> is_prime(-1)
    Traceback (most recent call last):
    ...
    ValueError: Value should be more one
    """
    if not isinstance(val, int):
        raise TypeError('Value should be of an integer type')
    elif val < 2:
        raise ValueError('Value should be more one')
    elif val > 100_000:
        raise ValueError('The value is too large')
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


