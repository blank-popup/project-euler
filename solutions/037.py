# -*- coding: utf-8 -*-


# 748317
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    for prime in aint.PRIMES:
        index = aint.PRIMES.index(prime)
        if index % 5000 == 0:
            logger.info(f'prime: {prime} ( {index} / {len(aint.PRIMES) - 1} )')
        if prime < 10:
            continue
        prime_string = str(prime)
        if int(prime_string[0]) not in aint.PRIMES or int(prime_string[-1]) not in aint.PRIMES:
            continue
        truncatable = True
        while True:
            prime_string = prime_string[1:]
            if int(prime_string) not in aint.PRIMES:
                truncatable = False
                break
            if len(prime_string) == 1:
                break
        if truncatable:
            pb = str(prime)
            while True:
                pb = pb[0:-1]
                if int(pb) not in aint.PRIMES:
                    truncatable = False
                    break
                if len(pb) == 1:
                    break
        if truncatable:
            solutions.append(prime)
    logger.info(solutions)
    logger.info(len(solutions))
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
