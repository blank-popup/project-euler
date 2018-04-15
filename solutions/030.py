# -*- coding: utf-8 -*-


# 443839


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    for number in range(2, 6 * 9 ** 5 + 1):
        q = number
        s = 0
        while q > 0:
            r = q % 10
            s += r ** 5
            q = q // 10
        if s == number:
            solutions.append(number)
    logger.info(sum(solutions))
    logger.info(solutions)

if __name__ == '__main__':
    main()
