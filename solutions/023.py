# -*- coding: utf-8 -*-


# 4179871


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    abundants = []
    for ii in range(1, 28124):
        divisors = aint.get_divisors(ii)
        if ii < sum(divisors) - ii:
            abundants.append(ii)
    logger.info(f'abundants: {abundants}')

    sums_of_abundant = [sum(c2) for c2 in aint.combinations_r(abundants, 2) if sum(c2) < 28124 ]
    sums_of_abundant = list(set(sums_of_abundant))
    sums_of_abundant.sort()
    logger.info(f'sums of abundant: {sums_of_abundant}')

    solutions = []
    number_previous = sums_of_abundant[0]
    for not_sa in range(1, number_previous):
        solutions.append(not_sa)
    for sa in sums_of_abundant:
        if sa > number_previous + 1:
            for not_sa in range(number_previous + 1, sa):
                solutions.append(not_sa)
        number_previous = sa
    for not_sa in range(sums_of_abundant[-1] + 1, 28124):
        solutions.append(not_sa)

    logger.info(solutions)
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
