# -*- coding: utf-8 -*-


# 153


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    fractions = [(3, 2)]
    solutions = []
    for ii in range(0, 999):
        fraction_next = (fractions[ii][0] + 2 * fractions[ii][1], fractions[ii][0] + fractions[ii][1])
        fractions.append(fraction_next)
    for fraction in fractions:
        if aint.count_digits(fraction[0]) > aint.count_digits(fraction[1]):
            solutions.append(1)
        else:
            solutions.append(0)
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
