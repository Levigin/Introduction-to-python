import pytest


def is_prime(val):
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


def test_is_prime():
    assert not is_prime(314), 'This number is not a prime'
    assert is_prime(7), "The number is prime"


def test_type():
    with pytest.raises(TypeError):
        is_prime(1.05)


def test_negative():
    with pytest.raises(ValueError):
        is_prime(-1)


def test_too_low():
    with pytest.raises(ValueError):
        is_prime(1)


def test_too_large():
    with pytest.raises(ValueError):
        is_prime(100_007)


if __name__ == '__main__':
    pytest.main()
