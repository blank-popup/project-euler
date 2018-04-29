# -*- coding: utf-8 -*-


# 26033
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def check_concantenate(A, B):
    if not aint.is_prime_number(int('{0}{1}'.format(A, B))):
        return False
    if not aint.is_prime_number(int('{0}{1}'.format(B, A))):
        return False
    return True

def check_concantenate_array(Solutions, Candidate):
    for solution in Solutions:
        if not check_concantenate(solution, Candidate):
            return False
    return True

def find_next_candidate(Seeds, Candidates):
    for candidate in Candidates:
        if check_concantenate_array(Seeds, candidate):
            yield candidate

def add_solution(Solutions, R):
    if R == 4:
        logger.info('Checking %s', str(Solutions[R][-1]))
    for candidate in find_next_candidate(Solutions[R][-1], aint.PRIMES[aint.PRIMES.index(Solutions[R][-1][-1]) + 1:]):
        Solutions[R + 1].append(list(Solutions[R][-1]) + [candidate])
        if R < 4:
            add_solution(Solutions, R + 1)
        else:
            logger.info('==============================')
            logger.info(Solutions[R + 1][-1])
            logger.info('==============================')

@abase.tick(logger)
def main():
    aint.PRIMES = aint.collect_prime_numbers(10000)
    aint.PRIMES = [aint.PRIMES[1]] + aint.PRIMES[3:]
    solutions = {ii: [] for ii in range(2, 6)}
    logger.info(solutions)
    for candidates in aint.combinations(aint.PRIMES, 2):
        if not check_concantenate(candidates[0], candidates[1]):
            continue
        solutions[2].append(candidates[:])
        add_solution(solutions, 2)
    logger.info(solutions[5])
    logger.info(sum(solutions[5][0]))

if __name__ == '__main__':
    main()
