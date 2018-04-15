# -*- coding: utf-8 -*-


# 871198282


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    data = abase.read_file(abase.dirpath_problems + '/p022_names.txt')
    data = data.replace('\"', '')
    names = data.split(',')
    names.sort()
    solutions = []
    for ii, name in enumerate(names):
        name = name.upper()
        worths = []
        for n in name:
            worths.append(ord(n) - ord('A') + 1)
        solutions.append((ii + 1, name, sum(worths)))

    logger.info(sum([s[0] * s[2] for s in solutions]))

if __name__ == '__main__':
    main()
