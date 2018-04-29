# -*- coding: utf-8 -*-


# 7273


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    data = abase.read_file(abase.dirpath_problems + '/p067_triangle.txt')
    rows = []
    for t in data.split('\n'):
        rows.append(t.split(' '))
    rows = rows[0:-1]

    for ii, _ in enumerate(rows):
        for jj, _ in enumerate(rows[ii]):
            rows[ii][jj] = (int(rows[ii][jj]), [])

    for ii in range(len(rows) - 1, 0, -1):
        for jj in range(0, ii):
            if rows[ii][jj][0] > rows[ii][jj + 1][0]:
                s = rows[ii - 1][jj][0] + rows[ii][jj][0]
                t = [jj] + rows[ii][jj][1]
            else:
                s = rows[ii - 1][jj][0] + rows[ii][jj + 1][0]
                t = [jj + 1] + rows[ii][jj + 1][1]
            rows[ii - 1][jj] = (s, t)

    logger.info(rows[0])

if __name__ == '__main__':
    main()
