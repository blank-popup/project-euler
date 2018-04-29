# -*- coding: utf-8 -*-


# 121313


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    def check_pattern5(Pattern):
        ones = [ii for ii, p in enumerate(Pattern) if p == 1]
        zeros = [ii for ii, p in enumerate(Pattern) if p == 0]
        for ii in range(0, 10):
            for jj in [9, 7, 3, 1]:
                value_base = ii * 10 ** ones[1] + jj
                value_check = 10 ** zeros[2] + 10 ** zeros[1] + 10 ** zeros[0]
                count = 0
                for kk in range(9, -1, -1):
                    if kk + 1 + count < 8:
                        break
                    value = value_base + kk * value_check
                    if value in aint.PRIMES:
                        count += 1
                    if count >= 8 and 10000 <= value < 100000:
                        solutions.append(value)
                        logger.info(f'{value}, {value_base}, {value_check}')

    pattern5 = [[1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0]]
    for Pattern in pattern5:
        check_pattern5(Pattern)

    def check_pattern6(Pattern):
        ones = [ii for ii, p in enumerate(Pattern) if p == 1]
        zeros = [ii for ii, p in enumerate(Pattern) if p == 0]
        for ii in range(0, 10):
            for jj in range(0, 10):
                for kk in [9, 7, 3, 1]:
                    value_base = ii * 10 ** ones[2] + jj * 10 ** ones[1] + kk
                    value_check = 10 ** zeros[2] + 10 ** zeros[1] + 10 ** zeros[0]
                    count = 0
                    for ll in range(9, -1, -1):
                        if ll + 1 + count < 8:
                            break
                        value = value_base + ll * value_check
                        if value in aint.PRIMES:
                            count += 1
                        if count >= 8 and 100000 <= value < 1000000:
                            solutions.append(value)
                            logger.info(f'{value}, {value_base}, {value_check}')

    pattern6 = [[1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0]]
    for Pattern in pattern6:
        check_pattern6(Pattern)
    logger.info(solutions)

if __name__ == '__main__':
    main()
