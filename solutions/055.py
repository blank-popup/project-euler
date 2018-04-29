# -*- coding: utf-8 -*-


# 249


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    for ii in range(10, 10000):
        lychrel = True
        number = ii
        for _ in range(0, 49):
            number += int(str(number)[::-1])
            if str(number) == str(number)[::-1]:
                lychrel = False
                break
        if lychrel:
            solutions.append(ii)

    # 4994, 8778, 9999
    # logger.info(solutions)
    logger.info(len(solutions))
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
