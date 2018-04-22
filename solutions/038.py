# -*- coding: utf-8 -*-


# 932718654


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    candidates = [(2, 5000, 10000), (3, 100, 334), (4, 25, 34), (5, 5, 10), (6, 3, 4), (9, 1, 2)]
    pandigital = set(ii for ii in range(1, 10))
    solutions = []
    for candidate in candidates:
        for c in range(candidate[2] - 1, candidate[1] - 1, -1):
            digitset = set()
            digit = ''
            for n in range(1, candidate[0] + 1):
                digitset = digitset | set(aint.get_digits(n * c))
                digit += str(n * c)
            if digitset == pandigital:
                solutions.append((digit, c, n))
    logger.info(solutions)
    solutions.sort(key=lambda x: x[0], reverse=True)
    logger.info(solutions[0])

if __name__ == '__main__':
    main()
