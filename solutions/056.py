# -*- coding: utf-8 -*-


# 972


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = {}
    for a in range(1, 100):
        for b in range(1, 100):
            c = a ** b
            solutions[(a, b)] = [c, aint.sum_of_digit(c)]

    key_max = max(solutions, key=lambda x: solutions[x][1])
    logger.info(solutions[key_max])

if __name__ == '__main__':
    main()
