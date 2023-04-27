import unittest


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


class TestFunc(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(4))

    def test_type(self):
        self.assertRaises(TypeError, is_prime, 1.05)
        self.assertRaises(TypeError, is_prime, "1.05")

    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)
            is_prime(100_007)


if __name__ == '__main__':
    unittest.main()
