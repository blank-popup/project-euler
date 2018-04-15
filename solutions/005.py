# -*- coding: utf-8 -*-


# 232792560


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    number = 20
    solutions = {}
    for ii in range(2, number + 1):
        factorizations = aint.factorize(ii)
        for factor, count in factorizations.items():
            if factor not in solutions.keys():
                solutions[factor] = count
            else:
                if count > solutions[factor]:
                    solutions[factor] = count

    solution = 1
    for prime, count in solutions.items():
        solution *= prime ** count

    logger.info(solution)

    # logger.info(2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19)

if __name__ == '__main__':
    main()
