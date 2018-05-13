# -*- coding: utf-8 -*-


# 5482660
# take a long time


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    pentagonals = [int(ii * (3 * ii - 1) / 2) for ii in range(1, 2500)]
    solutions = []
    for ii in range(1, 2499):
        if ii % 300 == 0:
            logger.info(f'ii: {ii}')
        for jj in range(0, ii):
            plus = False
            minus = False
            if pentagonals[ii] - pentagonals[jj] in pentagonals:
                # logger.info(pentagonals[ii] - pentagonals[jj], '-', ii, jj)
                minus = True
            if pentagonals[ii] + pentagonals[jj] in pentagonals:
                # logger.info(pentagonals[ii] + pentagonals[jj], '+', ii, jj)
                plus = True
            if plus and minus:
                solutions.append((pentagonals[ii], pentagonals[jj], (pentagonals[ii] + pentagonals[jj]), (pentagonals[ii] - pentagonals[jj]), ii, jj))
    logger.info(len(solutions))
    logger.info(solutions)

if __name__ == '__main__':
    main()
