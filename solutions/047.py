# -*- coding: utf-8 -*-


# 134043


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = {}
    count_factor = 4
    consecutive = 0
    ii = 1
    while True:
        solutions[ii] = aint.factorize(ii)
        if len(solutions[ii]) == count_factor:
            consecutive += 1
        else:
            consecutive = 0
        if consecutive == count_factor:
            logger.info(', '.join([str(jj) for jj in range(ii - count_factor + 1, ii + 1)]))
            break
        if ii % 2000 == 0:
            logger.info(f'{ii} have {len(solutions[ii])} distinct factors')
        ii += 1

if __name__ == '__main__':
    main()
