# -*- coding: utf-8 -*-


# 73682


# coins = [200, 100, 50, 20, 10, 5, 2, 1]
# [1, 2, 4, 10, 20, 40, 100, 200]

from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solution = 0
    table = aint.get_table_way_sums_of_constraints(200, [1, 2, 5, 10, 20, 50, 100, 200])
    for row in table:
        solution += row[-1]
    logger.info(solution)

    # solutions = []
    # for a in range(0, 2):
    #     for b in range(0, 3):
    #         if a * 200 + b * 100 > 200:
    #             break
    #         for c in range(0, 5):
    #             if a * 200 + b * 100 + c * 50 > 200:
    #                 break
    #             for d in range(0, 11):
    #                 if a * 200 + b * 100 + c * 50 + d * 20 > 200:
    #                     break
    #                 for e in range(0, 21):
    #                     if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 > 200:
    #                         break
    #                     for f in range(0, 41):
    #                         if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 > 200:
    #                             break
    #                         for g in range(0, 101):
    #                             if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 > 200:
    #                                 break
    #                             for h in range(0, 201):
    #                                 v = a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 + h
    #                                 if v == 200:
    #                                     solutions.append((a, b, c, d, e, f, g, h))
    #                                     break

    # logger.info(len(solutions))

if __name__ == '__main__':
    main()
