# -*- coding: utf-8 -*-


# 55
# take a long time

from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    candidates = []
    for prime in aint.PRIMES:
        candidates.append(aint.get_digits(prime))
    solutions = []

    for prime in aint.PRIMES:
        index = aint.PRIMES.index(prime)
        if index % 5000 == 0:
            logger.info(f'prime: {prime} ( {index} / {len(aint.PRIMES) - 1} )')
        rs = aint.get_rotations(aint.get_digits(prime))
        is_circular_prime = True
        for r in rs:
            if r not in candidates:
                is_circular_prime = False
                break
        if is_circular_prime:
            solutions.append(prime)

    logger.info(solutions)
    logger.info(len(solutions))

if __name__ == '__main__':
    main()
