# -*- coding: utf-8 -*-


# 210


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    candidate = ''
    for ii in range(0, 200000):
        candidate += str(ii)
    solution = 1
    for ii in range(0, 7):
        solution *= int(candidate[10 ** ii])
    logger.info(solution)

if __name__ == '__main__':
    main()
