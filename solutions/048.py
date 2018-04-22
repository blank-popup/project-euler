# -*- coding: utf-8 -*-


# 9110846700


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    logger.info(sum([ii ** ii for ii in range(1, 1001)]))

if __name__ == '__main__':
    main()
