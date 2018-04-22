# -*- coding: utf-8 -*-


# 840


# a <= b <= c
# a + b + c = p
# a + b > c

# a**2 + b**2 = c**2
# p <= 1000

from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = {}
    for p in range(1000, 0, -1):
        solutions[p] = []
        for c in range(int((p + 2) / 3), int((p + 1) / 2)):
            for b in range(int((p - c + 1) / 2), c + 1):
                a = p - c - b
                # if a > b or b > c or a > c or a + b <= c:
                #     logger.info(f'abnormal: {p} {a} {b} {c}')
                #     continue
                if a ** 2 + b ** 2 == c ** 2:
                    solutions[p].append((p, a, b, c))
    logger.info(solutions)
    key_max = max(solutions.keys(), key=lambda x: len(solutions[x]))
    logger.info(solutions[key_max])
    logger.info(key_max)

if __name__ == '__main__':
    main()
