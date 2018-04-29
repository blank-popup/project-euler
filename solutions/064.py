# -*- coding: utf-8 -*-


# 1322


from aha import aha_base as abase
from aha import aha_real as areal

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = {}
    for ii in range(1, 10001):
        solutions[ii] = areal.make_continued_fraction_from_root(ii)
    count_odd_period = 0
    for solution in solutions:
        if solutions[solution].repetend_length % 2 == 1:
            count_odd_period += 1
    logger.info(count_odd_period)

if __name__ == '__main__':
    main()
