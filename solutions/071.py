# -*- coding: utf-8 -*-


# 428570


from aha import aha_base as abase
from aha import aha_rational as arat

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    # k       3                    3
    # -   <   -      <=>     k  <  - * n
    # n       7                    7
    for ii in range(2, 1000001):
        if ii % 7 == 0:
            k = 3 * ii / 7 - 1
        else:
            k = 3 * ii // 7
        solutions.append((ii, k, k / ii))
    solutions.sort(key=lambda x: x[2])
    f = arat.Fraction(solutions[-1][1], solutions[-1][0])
    numerator, denominator = f.numerator, f.denominator
    logger.info(solutions[-1])
    logger.info(f'{numerator} / {denominator}')

if __name__ == '__main__':
    main()
