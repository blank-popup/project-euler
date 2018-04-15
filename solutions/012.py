# -*- coding: utf-8 -*-


# 76576500


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    for triangle_number in aint.generate_N_angle_number(3):
        factors = aint.factorize(triangle_number)
        count = aint.count_divisor(factors)
        if count > 500:
            logger.info(f'{triangle_number}')
            break

if __name__ == '__main__':
    main()
