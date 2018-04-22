# -*- coding: utf-8 -*-


# 7652413


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    aint.PRIMES = aint.collect_prime_numbers(10000000)
    solutions = []
    for ii in range(len(aint.PRIMES) - 1, -1, -1):
        digits = aint.get_digits(aint.PRIMES[ii])
        pandigital = set(ii for ii in range(1, len(digits) + 1))
        if set(digits) == pandigital:
            solutions.append(aint.PRIMES[ii])
    logger.info(len(aint.PRIMES))
    logger.info(len(solutions))
    logger.info(solutions[0])

if __name__ == '__main__':
    main()
