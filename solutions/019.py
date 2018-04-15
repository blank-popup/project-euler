# -*- coding: utf-8 -*-


# 171


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    day = 2
    solutions = []

    for ii in range(1901, 2001):
        if ii % 400 == 0 or ii % 100 != 0 and ii % 4 == 0:
            dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for jj in range(1, 13):
            if ii != 2000 or jj != 12:
                day = (dates[jj - 1] + day) % 7
                if day == 0:
                    if jj == 12:
                        solutions.append((ii + 1, 1))
                    else:
                        solutions.append((ii, jj + 1))

    logger.info(solutions)
    logger.info(len(solutions))

if __name__ == '__main__':
    main()
