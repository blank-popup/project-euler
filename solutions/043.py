# -*- coding: utf-8 -*-


# 16695334890


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    candidates = aint.permutations(list(ii for ii in range(0, 10)), 10)
    candidates = [c for c in candidates if c[0] != 0]
    divisors = aint.collect_prime_numbers(19)
    solutions = []
    for candidate in candidates:
        divisible = True
        for ii in range(0, 7):
            if (candidate[ii + 1] * 100 + candidate[ii + 2] * 10 + candidate[ii + 3]) % divisors[ii] != 0:
                divisible = False
                break
        if divisible:
            solutions.append(candidate)

    logger.info(solutions)
    solutions = [s[0] * 1000000000 + s[1] * 100000000 + s[2] * 10000000 + s[3] * 1000000 + s[4] * 100000 + s[5] * 10000 + s[6] * 1000 + s[7] * 100 + s[8] * 10 + s[9] for s in solutions]
    logger.info(solutions)
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
