# -*- coding: utf-8 -*-


# solution


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = set()
    not_solution = set()
    L_limit = 1500000
    for m in range(2, int((L_limit / 2) ** 0.5)):
        n = 1
        for n in range(1, m):
            L = 2 * m ** 2 + 2 * m * n
            if L > L_limit:
                break
            if (m + n) % 2 == 1 and aint.gcd(m, n) == 1:
                while L <= L_limit:
                    if L not in solutions:
                        solutions.add(L)
                    else:
                        not_solution.add(L)
                    L += 2 * m ** 2 + 2 * m * n
    logger.info(len(solutions) - len(not_solution))

if __name__ == '__main__':
    main()
