# -*- coding: utf-8 -*-


# 4613732


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    fibonacci = [1, 2]
    while fibonacci[-1] <= 4000000:
        fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])

    solutions = [ff for ff in fibonacci if ff % 2 == 0]
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
