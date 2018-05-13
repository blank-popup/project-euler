# -*- coding: utf-8 -*-


# 669171001


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    logger.info(1 + 16 * 500 * 501 * 1001 // 6 + 4 * 500 * 501 // 2 + 4 * 500)

if __name__ == '__main__':
    main()
