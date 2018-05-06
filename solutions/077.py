# -*- coding: utf-8 -*-


# 71

from aha import aha_base as abase
from aha import aha_integer as aint
from aha import aha_rational as arat

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    table = []
    n = 2
    while True:
        table = aint.get_table_way_sums_of_constraints(n, aint.PRIMES, table)
        count = 0
        for row in table:
            count += row[-1]
        if count > 5000:
            break
        n += 1
        # counts, table = aint.get_table_way_sums_of_constraints(n, aint.PRIMES, table)
        # if counts[-1] > 5000:
        #     break
        # n += 1
        # if n % 100 == 0:
        #     logger.info(n)
    logger.info(n)

if __name__ == '__main__':
    main()
