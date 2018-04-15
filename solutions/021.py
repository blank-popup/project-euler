# -*- coding: utf-8 -*-


# 31626


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    sum_divisors = {}
    solutions = set()
    for ii in range(2, 10000):
        sum_divisors[ii] = sum(aint.get_divisors(ii)) - ii
    for ii in range(2, 10000):
        if ii != sum_divisors[ii] and sum_divisors[ii] in sum_divisors and sum_divisors[sum_divisors[ii]] == ii:
            logger.info(f'{ii}: {sum_divisors[ii]}')
            solutions.add(ii)
            solutions.add(sum_divisors[ii])
    logger.info(solutions)
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
