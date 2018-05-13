# -*- coding: utf-8 -*-


# 31875000 ([a, b, c] = [200, 375, 425])


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    for a in range(1, 1001):
        for b in range(a + 1, 1001):
            c = 1000 - a - b
            if b >= c:
                break
            if a ** 2 + b ** 2 == c ** 2:
                logger.info(f'[a, b, c] = {str([a, b, c])}')
                logger.info(f'abc = [{a * b * c}]')

if __name__ == '__main__':
    main()
