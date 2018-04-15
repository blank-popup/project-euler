# -*- coding: utf-8 -*-


# 906609
# 993 * 913


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = [(ii * jj, ii, jj) for ii in range(999, 99, -1) for jj in range(ii, 99, -1)]
    solutions.sort(reverse=True, key=lambda x : x[0])
    for solution in solutions:
        if str(solution[0]) == str(solution[0])[::-1]:
            logger.info(solution)
            break

if __name__ == '__main__':
    main()
