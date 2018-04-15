# -*- coding: utf-8 -*-


# solution


import math
import itertools
import fractions
import decimal

from aha import aha_base as abase
from aha import aha_integer as aint
from aha import aha_rational as arat
from aha import aha_real as areal

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    logger.info(777)

if __name__ == '__main__':
    main()
