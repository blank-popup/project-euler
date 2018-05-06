# -*- coding: utf-8 -*-


# 7295372


from aha import aha_base as abase
from aha import aha_rational as arat

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    farey = arat.get_farey_sequence(12000)
    logger.info(len(farey))
    index_from = farey.index((1, 3))
    index_to = farey.index((1, 2))
    logger.info(index_to - index_from - 1)

if __name__ == '__main__':
    main()
