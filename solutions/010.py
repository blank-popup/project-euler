# -*- coding: utf-8 -*-


# 142913828922


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    aint.PRIMES = aint.collect_prime_numbers(2000000)
    logger.info(len(aint.PRIMES))
    logger.info(sum(aint.PRIMES))

if __name__ == '__main__':
    main()
