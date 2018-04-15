# -*- coding: utf-8 -*-


# 2783915460


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    number_used = []
    number_unused = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index_target = 999999
    index_remain = index_target
    for ii in range(9, -1, -1):
        count_chunk = aint.factorial(ii)
        count_subtraction = 0
        while index_remain >= count_chunk:
            index_remain -= count_chunk
            count_subtraction += 1
        number_used.append(number_unused.pop(count_subtraction))
        logger.info(f'{ii} {count_subtraction} {index_remain} {count_chunk} {number_used} {number_unused}')

    # for ii, value in enumerate(aint.meta_permutations(10, 10)):
    #     if ii == 999999 or ii == 999998 or ii == 1000000:
    #         logger.info(f'{ii} {value}')
    #         break

if __name__ == '__main__':
    main()
