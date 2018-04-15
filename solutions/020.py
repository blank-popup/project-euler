# -*- coding: utf-8 -*-


# 648


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solution = aint.factorial(100)
    logger.info(aint.sum_of_digit(solution))

if __name__ == '__main__':
    main()
