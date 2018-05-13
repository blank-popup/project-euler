# -*- coding: utf-8 -*-


# 510510


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    aint.PRIMES = aint.collect_prime_numbers(1000001)
    solution = 1
    for prime in aint.PRIMES:
        if solution * prime > 1000000:
            break
        solution *= prime
    logger.info(solution)

if __name__ == '__main__':
    main()
