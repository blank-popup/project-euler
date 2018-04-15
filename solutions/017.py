# -*- coding: utf-8 -*-


# 21124


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    numbers_0 = ['one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']
    numbers_10 = ['ten', 'eleven', 'tewlve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    numbers_20 = ['twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']
    number_100 = 'hundred'
    number_and = 'and'

    solutions = []
    for n in range(1, 1000):
        n2 = n // 100
        n1 = (n - n2 * 100) // 10
        n0 = n % 10

        number = ''
        if n2 > 0:
            number += numbers_0[n2 - 1] + number_100
            if n1 != 0 or n0 != 0:
                number += number_and
        if n1 == 0:
            if n0 > 0:
                number += numbers_0[n0 - 1]
        elif n1 == 1:
            number += numbers_10[n0]
        else:
            number += numbers_20[n1 - 2]
            if n0 > 0:
                number += numbers_0[n0 - 1]
        solutions.append(number)

    solutions.append('onethousand')

    logger.info(sum([len(s) for s in solutions]))

if __name__ == '__main__':
    main()


# #    0  1  2  3  4  5  6  7  8  9
# # 0     1  2  3  4  5  6  7  8  9
# # 1 10 11 12 13 14 15 16 17 18 19
# # 2 20 21 22 23 24 25 26 27 28 29
# # 3 30 31                      39
# # 4 40 41                      49
# # 5
# # 6
# # 7
# # 8
# # 9 90 91                      99

# # 100 101 102 ... 199
# # 200 201 202 ... 299
# # 300 301 302 ... 399

# # 900 901 902 ... 999
# # 100 200 300 ... 900
