# -*- coding: utf-8 -*-


# 5777


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    aint.PRIMES = aint.collect_prime_numbers(10000)
    candidates = list(set(range(2, 10000)) - set(aint.PRIMES) - set([ii for ii in range(2, 10000) if ii % 2 == 0]))
    candidates.sort()
    solutions = []
    for candidate in candidates:
        a = 1
        conjecture = False
        while 2 * a ** 2 < candidate:
            b = candidate - 2 * a ** 2
            if b in aint.PRIMES:
                conjecture = True
                solutions.append((candidate, True, b, a))
                break
            a += 1
        solutions.append((candidate, conjecture))
    for s in solutions:
        if not s[1]:
            logger.info(s)

if __name__ == '__main__':
    main()
