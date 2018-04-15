# -*- coding: utf-8 -*-


# 4782


from logging import root
from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    # root_5 = 5 ** 0.5
    # alpha = (1 + root_5) / 2
    # beta = (1 - root_5) / 2
    # n = 1
    # while True:
    #     fibonacci = int(alpha ** n / root_5 - beta ** n / root_5)
    #     if fibonacci >= 10 ** 999:
    #         break
    #     logger.info(f'{n} {fibonacci}')
    #     n += 1

    fibonacci = [1, 1]
    while fibonacci[-1] <= 10 ** 999:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    logger.info(len(fibonacci))

if __name__ == '__main__':
    main()
