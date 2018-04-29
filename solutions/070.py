# -*- coding: utf-8 -*-


# 8319823


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    bound = 10000000
    aint.PRIMES = aint.collect_prime_numbers(bound)
    logger.info(len(aint.PRIMES))
    solutions = []
    for ii in range(0, len(aint.PRIMES)):
        for jj in range(ii + 1, len(aint.PRIMES)):
            n = aint.PRIMES[ii] * aint.PRIMES[jj]
            if n >= bound:
                break
            totient = (aint.PRIMES[ii] - 1) * (aint.PRIMES[jj] - 1)
            ratio = n / totient
            solutions.append((n, aint.PRIMES[ii], aint.PRIMES[jj], totient, ratio))
    solutions.sort(key=lambda x: x[4])
    for solution in solutions:
        ns = aint.get_digits(solution[0])
        ns.sort()
        totients = aint.get_digits(solution[3])
        totients.sort()
        if ns == totients:
            logger.info(solution)
            break

if __name__ == '__main__':
    main()
