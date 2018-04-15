# -*- coding: utf-8 -*-


# 233168


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    count_5 = 999 // 5
    count_3 = 999 // 3
    count_15 = 999 // 15
    sum_5 = count_5 * (count_5 + 1) / 2 * 5
    sum_3 = count_3 * (count_3 + 1) / 2 * 3
    sum_15 = count_15 * (count_15 + 1) / 2 * 15
    solution = int(sum_5 + sum_3 - sum_15)
    logger.info(solution)

if __name__ == '__main__':
    main()
