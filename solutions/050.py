# -*- coding: utf-8 -*-


# 997651
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = {}
    for ii in range(0, len(aint.PRIMES)):
        index_start = 0
        index_end = 1
        sum_target = aint.PRIMES[index_start]
        while True:
            if sum_target < aint.PRIMES[ii]:
                index_end += 1
                sum_target += aint.PRIMES[index_end - 1]
                if index_end - 1 >= ii:
                    break
            elif sum_target > aint.PRIMES[ii]:
                index_start += 1
                sum_target -= aint.PRIMES[index_start - 1]
            else:
                solutions[aint.PRIMES[ii]] = (index_end - index_start, index_start, index_end)
                break
        if ii % int(len(aint.PRIMES) / 40) == 0:
            logger.info(f'Checked {ii} / {len(aint.PRIMES)}')

    key_max = max(solutions.keys(), key=lambda x: solutions[x][0])
    logger.info(key_max)
    logger.info(solutions[key_max])

if __name__ == '__main__':
    main()
