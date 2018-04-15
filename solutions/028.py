# -*- coding: utf-8 -*-


# 669171001

# 1: 1
# 2: 3 + 5 + 7 + 9
# 3: 13 + 17 + 21 + 25
# 4: 31 + 37 + 43 + 49
# 5: 57 + 65 + 73 + 81
# ...
# 501:

# 3 13 31 57 ...
# 4n**2 -2n +1

# 16n**2 -8n +4 + 12n
# 16n**2 +4n +4

from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    logger.info(1 + 16 * 500 * 501 * 1001 // 6 + 4 * 500 * 501 // 2 + 4 * 500)

if __name__ == '__main__':
    main()
