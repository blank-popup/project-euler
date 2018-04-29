# -*- coding: utf-8 -*-


# 4075


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    total = 0
    for nn in range(1, 101):
        count = 0
        for rr in range(0, int((nn + 2) / 2)):
            combination = aint.factorial(nn) / aint.factorial(rr) / aint.factorial(nn - rr)
            if combination > 1000000:
                count += 1
        if count > 0:
            if nn % 2 == 0:
                total += 2 * count - 1
            else:
                total += 2 * count
    logger.info(total)
    # 1: 0 1 : 0
    # 2: 0 1 2 : 1
    # 3: 0 1 2 3 : 1
    # 4: 0 1 2 3 4 : 2
    # 5: 0 1 2 3 4 5 : 2
    # 6: 0 1 2 3 4 5 6 : 3
    # 7: 0 1 2 3 4 5 6 7 : 3

if __name__ == '__main__':
    main()
