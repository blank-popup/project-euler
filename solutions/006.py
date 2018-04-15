# -*- coding: utf-8 -*-


# 25164150


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    sum_of_square_100 = 100 * (100 + 1) * (2 * 100 + 1) / 6
    square_of_summ_100 = (100 * (100 + 1) / 2) ** 2
    logger.info(int(square_of_summ_100 - sum_of_square_100))

if __name__ == '__main__':
    main()
