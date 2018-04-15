# -*- coding: utf-8 -*-


# -59231
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    bs = [p for p in aint.PRIMES if p <= 1000]
    solutions = {}
    for a in range(-999, 1000):
        if a % 50 == 0:
            logger.info(f'a: {a} / 999')
        for b in bs:
            n = 0
            while n ** 2 + a * n + b in aint.PRIMES:
                n += 1
            if n > 1:
                solutions[(a, b)] = n
                # ===== [  a], [  b], [  n] =====
                # ===== [ -61 ], [ 971 ], [ 71 ] =====
                # ===== [ -59 ], [ 911 ], [ 70 ] =====
                # ===== [ -57 ], [ 853 ], [ 69 ] =====
                # ===== [ -55 ], [ 797 ], [ 68 ] =====
                # ===== [ -53 ], [ 743 ], [ 67 ] =====
                # ===== [ -51 ], [ 691 ], [ 66 ] =====
                # ===== [ -49 ], [ 641 ], [ 65 ] =====
                # ===== [ -47 ], [ 593 ], [ 64 ] =====
                # ===== [ -45 ], [ 547 ], [ 63 ] =====
                # ===== [ -43 ], [ 503 ], [ 62 ] =====
                # ===== [ -41 ], [ 461 ], [ 61 ] =====
                # ===== [ -39 ], [ 421 ], [ 60 ] =====
                # ===== [ -37 ], [ 383 ], [ 59 ] =====
                # ===== [ -35 ], [ 347 ], [ 58 ] =====
                # ===== [ -33 ], [ 313 ], [ 57 ] =====
                # ===== [ -31 ], [ 257 ], [ 32 ] =====
                # ===== [ -31 ], [ 281 ], [ 56 ] =====
                # ===== [ -29 ], [ 227 ], [ 31 ] =====
                # ===== [ -29 ], [ 251 ], [ 55 ] =====
                # ===== [ -27 ], [ 223 ], [ 54 ] =====
                # ===== [ -25 ], [ 197 ], [ 53 ] =====
                # ===== [ -23 ], [ 173 ], [ 52 ] =====
                # ===== [ -21 ], [ 151 ], [ 51 ] =====
                # ===== [ -19 ], [ 131 ], [ 50 ] =====
                # ===== [ -17 ], [ 113 ], [ 49 ] =====
                # ===== [ -15 ], [ 97 ], [ 48 ] =====
                # ===== [ -13 ], [ 83 ], [ 47 ] =====
                # ===== [ -11 ], [ 71 ], [ 46 ] =====
                # ===== [ -9 ], [ 61 ], [ 45 ] =====
                # ===== [ -7 ], [ 53 ], [ 44 ] =====
                # ===== [ -5 ], [ 47 ], [ 43 ] =====
                # ===== [ -3 ], [ 43 ], [ 42 ] =====
                # ===== [ -1 ], [ 41 ], [ 41 ] =====
                # ===== [ 1 ], [ 41 ], [ 40 ] =====
                # ===== [ 3 ], [ 43 ], [ 39 ] =====
                # ===== [ 5 ], [ 47 ], [ 38 ] =====
                # ===== [ 7 ], [ 53 ], [ 37 ] =====
                # ===== [ 9 ], [ 61 ], [ 36 ] =====
                # ===== [ 11 ], [ 71 ], [ 35 ] =====
                # ===== [ 13 ], [ 83 ], [ 34 ] =====
                # ===== [ 15 ], [ 97 ], [ 33 ] =====
                # ===== [ 17 ], [ 113 ], [ 32 ] =====
                # ===== [ 19 ], [ 131 ], [ 31 ] =====

    keys = max(solutions.keys(), key=lambda x: solutions[x])
    logger.info(keys)
    logger.info(keys[0] * keys[1])

if __name__ == '__main__':
    main()