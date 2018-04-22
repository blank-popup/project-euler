# -*- coding: utf-8 -*-


# 296962999629


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def is_permutation(aa, bb):
    list_aa = aint.get_digits(aa)
    list_aa.sort()
    list_bb = aint.get_digits(bb)
    list_bb.sort()
    return list_aa == list_bb

@abase.tick(logger)
def main():
    solutions = []
    aint.PRIMES = aint.collect_prime_numbers(10000)
    aint.PRIMES = [p for p in aint.PRIMES if p > 999]
    solutions = []
    for ii in range(0, len(aint.PRIMES) - 2):
        for jj in range(ii + 1, len(aint.PRIMES) - 1):
            if not is_permutation(aint.PRIMES[ii], aint.PRIMES[jj]):
                continue
            pp = 2 * aint.PRIMES[jj] - aint.PRIMES[ii]
            if pp > 9999:
                break
            if pp in aint.PRIMES:
                if is_permutation(aint.PRIMES[ii], pp):
                    solutions.append((aint.PRIMES[ii], aint.PRIMES[jj], pp))
    logger.info(solutions)
    for solution in solutions:
        logger.info(f'{solution[0]}{solution[1]}{solution[2]}')

if __name__ == '__main__':
    main()
