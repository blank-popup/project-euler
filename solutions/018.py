# -*- coding: utf-8 -*-


# 1074


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


    rows = []

    for t in triangle.split('\n'):
        rows.append(t.split(' '))

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
