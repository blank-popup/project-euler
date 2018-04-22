# -*- coding: utf-8 -*-


# 872187


from aha import aha_base as abase
from aha import aha_integer as aint
from aha import aha_rational as arat

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    for ii in range(1, 1000000):
        value = str(ii)
        if value == value[::-1]:
            value_bin = aint.convert_base(value, 2, 10)
            if value_bin == value_bin[::-1]:
                solutions.append(ii)

    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
