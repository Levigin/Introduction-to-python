import logging

FORMAT = '%(asctime)s %(name)s - %(lineno)s line(s) - %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, filename='logs.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def is_prime(val):
    if not isinstance(val, int):
        logging.error(f'Invalid type {type(val)}')
        raise TypeError('Value should be of an integer type')
    elif val < 2:
        logging.error('Value should be is out of range [2, 100000]')
        raise ValueError('Value should be more one')
    elif val > 100_000:
        logging.error('Value should be is out of range [2, 100000]')
        raise ValueError('The value is too large')
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            logging.info(f'{val}, is compound')
            return False
    logging.info(f'{val}, is prime')
    return True


if __name__ == '__main__':
    is_prime(2)
    is_prime(7)
    is_prime(1.05)
    # is_prime(-1)
    # is_prime(100_007)