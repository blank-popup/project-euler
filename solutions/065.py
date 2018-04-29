# -*- coding: utf-8 -*-


# 272


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    es = [2]
    length = 100
    for ii in range(0, length - 1):
        if ii % 3 == 1:
            es.append((ii // 3 + 1) * 2)
        else:
            es.append(1)
    logger.info(es[0:length])

    numerator_e = 0
    denominator_e = 1
    for ii in range(length - 1, 0, -1):
        numerator_e += es[ii] * denominator_e
        numerator_e, denominator_e = denominator_e, numerator_e
    numerator_e += es[0] * denominator_e

    logger.info(f'{numerator_e} / {denominator_e}')
    logger.info(f'{aint.sum_of_digit(numerator_e)}')

if __name__ == '__main__':
    main()
