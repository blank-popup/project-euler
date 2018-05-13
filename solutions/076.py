# -*- coding: utf-8 -*-


# 190569291


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    count = 0
    table = aint.get_table_partitions(100)
    for row in table:
        count += row[-1]
    logger.info(count - 1)

if __name__ == '__main__':
    main()
