# -*- coding: utf-8 -*-


# 983


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    numbers = list(range(1, 1000))
    solutions = {}
    for number in numbers:
        n = number
        while n % 2 == 0:
            n = int(n / 2)
        while n % 5 == 0:
            n = int(n / 5)
        if n == 1:
            solutions[number] = 0
        else:
            k = 1
            while (10 ** k - 1) % n != 0:
                k += 1
            solutions[number] = k

    logger.info(max(solutions.keys(), key=lambda x: solutions[x]))

if __name__ == '__main__':
    main()
