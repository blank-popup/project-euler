# -*- coding: utf-8 -*-


# 40730


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    fs = [aint.factorial(ii) for ii in range(0, 10)]
    solutions = []

    for ii in range(10, 2540161):
        digits = aint.get_digits(ii)
        s = 0
        for d in digits:
            s += fs[d]
        if ii == s:
            solutions.append(ii)

    logger.info(solutions)
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
