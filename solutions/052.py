# -*- coding: utf-8 -*-


# 142857


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

print(__file__)

@abase.tick(logger)
def main():
    solutions = []
    exp = 0
    while True:
        for ii in range(10 ** exp, 10 ** (exp + 1)):
            if 6 * ii > 10 ** (exp + 1):
                exp += 1
                break
            list_1 = aint.get_digits(ii)
            list_2 = aint.get_digits(2 * ii)
            list_1.sort()
            list_2.sort()
            if list_1 != list_2:
                continue
            list_3 = aint.get_digits(3 * ii)
            list_3.sort()
            if list_1 != list_3:
                continue

            list_4 = aint.get_digits(4 * ii)
            list_4.sort()
            if list_1 != list_4:
                continue
            list_5 = aint.get_digits(5 * ii)
            list_5.sort()
            if list_1 != list_5:
                continue
            list_6 = aint.get_digits(6 * ii)
            list_6.sort()
            if list_1 != list_6:
                continue
            solutions.append(ii)
            break
        logger.info(f'Checked exp [{exp - 1}]')
        if len(solutions) > 0:
            break
    logger.info(solutions)

if __name__ == '__main__':
    main()
