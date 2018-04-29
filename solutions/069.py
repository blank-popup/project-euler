# -*- coding: utf-8 -*-


# 510510


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    aint.PRIMES = aint.collect_prime_numbers(1000001)
    solution = 1
    for prime in aint.PRIMES:
        if solution * prime > 1000000:
            break
        solution *= prime
    logger.info(solution)

if __name__ == '__main__':
    main()

# [2021-01-01 18:11:46,426][aha.069][INFO] Start!!!
# [2021-01-01 20:04:56,432][aha.069][INFO] (510510, 92160, 5.539388020833333)
# [2021-01-01 20:04:56,679][aha.069][INFO] time: [6790.2528959]
# @abase.tick(logger)
# def main():
#     primes = aint.get_prime_numbers(1000001)
#     solutions = []
#     for ii in range(2, 1000001):
#         totient = aint.get_euler_totient(ii, primes)
#         solutions.append((ii, totient, ii / totient))
#         logger.info('{0} : {1} : {2}'.format(ii, totient, ii / totient))
#     solutions.sort(key=lambda  x: x[2])
#     for solution in solutions:
#         logger.info(solution)

# if __name__ == '__main__':
#     main()
