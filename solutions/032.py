# -*- coding: utf-8 -*-


# 45228


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    candidates = aint.permutations(list(range(1, 10)), 9)
    solutions = []

    for cs in candidates:
        multiplicand = cs[0]
        multiplier = cs[1] * 1000 + cs[2] * 100 + cs[3] * 10 + cs[4]
        product = cs[5] * 1000 + cs[6] * 100 + cs[7] * 10 + cs[8]
        if multiplicand * multiplier == product:
            solutions.append(cs)
        multiplicand = cs[0] * 10 + cs[1]
        multiplier = cs[2] * 100 + cs[3] * 10 + cs[4]
        product = cs[5] * 1000 + cs[6] * 100 + cs[7] * 10 + cs[8]
        if multiplicand * multiplier == product:
            solutions.append(cs)

    logger.info(solutions)
    logger.info(sum(set([s[5] * 1000 + s[6] * 100 + s[7] * 10 + s[8] for s in solutions])))

if __name__ == '__main__':
    main()
