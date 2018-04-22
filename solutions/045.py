# -*- coding: utf-8 -*-


# 1533776805
# [(1533776805, 27692)]

from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    triangles = [int(ii * (ii + 1) / 2) for ii in range(1, 120000)]
    pentagonals = [int(ii * (3 * ii - 1) / 2) for ii in range(1, 40000)]
    hexagonals = [int(ii * (2 * ii - 1)) for ii in range(1, 30000)]
    solutions = []

    for ii in range(143, 29999):
        if hexagonals[ii] in pentagonals:
            if hexagonals[ii] in triangles:
                solutions.append((hexagonals[ii], ii))

    logger.info(f'{triangles[284]} {pentagonals[164]} {hexagonals[142]}')
    logger.info(solutions)

if __name__ == '__main__':
    main()
