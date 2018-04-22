# -*- coding: utf-8 -*-


# 162


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    triangles = [int(ii * (ii + 1) / 2) for ii in range(0, 30)]
    logger.info(triangles)
    data = abase.read_file(abase.dirpath_problems + '/p042_words.txt')
    data = data.replace('\"', '')
    words = data.split(',')
    solutions = []
    for word in words:
        value = 0
        for s in word:
            value += ord(s) - ord('A') + 1
        if value in triangles:
            solutions.append(word)
    logger.info(len(solutions))
    logger.info(solutions)

if __name__ == '__main__':
    main()
