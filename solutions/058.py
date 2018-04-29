# -*- coding: utf-8 -*-


# 26241
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    diagonals = 0
    n = 1
    while True:
        diagonals += 1 if aint.is_prime_number((2 * n - 1) ** 2 + 2 * n) else 0
        diagonals += 1 if aint.is_prime_number((2 * n - 1) ** 2 + 4 * n) else 0
        diagonals += 1 if aint.is_prime_number((2 * n - 1) ** 2 + 6 * n) else 0
        # diagonals += 1 if aint.is_prime_number((2 * n - 1) ** 2 + 8 * n) else 0
        if diagonals / (4 * n + 1) < 0.1:
            break
        n += 1
        if n % 500 == 0:
            logger.info(f'{n} {diagonals}, {diagonals / (4 * n + 1)}')
    logger.info(2 * n + 1)

if __name__ == '__main__':
    main()
