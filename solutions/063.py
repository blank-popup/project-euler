# -*- coding: utf-8 -*-


# 49


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    for a in range(1, 10):
        b = 1
        difference = 100
        while True:
            value = a ** b
            count_digits = aint.count_digits(value)
            if count_digits == b:
                solutions.append((a, b))
            if b - count_digits > difference:
                break
            else:
                difference = b - count_digits
            b += 1
    logger.info(solutions)
    logger.info(len(solutions))

if __name__ == '__main__':
    main()
