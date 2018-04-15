# -*- coding: utf-8 -*-


# 31875000 ([a, b, c] = [200, 375, 425])


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    for a in range(1, 1001):
        for b in range(a + 1, 1001):
            c = 1000 - a - b
            if b >= c:
                break
            if a ** 2 + b ** 2 == c ** 2:
                logger.info(f'[a, b, c] = {str([a, b, c])}')
                logger.info(f'abc = [{a * b * c}]')

if __name__ == '__main__':
    main()


# a < b < c

# a ** 2 = c ** 2 - b ** 2 = (c + b)(c - b)


# c - b = 1
# c + b = 1 4 9 16 25 36 49 ...
# 1 0
# 5 4
# 13 12
# 25 24
# 41 40

# (ka) ** 2 = (kc) ** 2 - (kb) ** 2 = (kc + kb)(kc - kb)

# ka + kb + kc = 1000

# a + b + c = 1000, 500, 250, 200, 125, 100, 50, 40, 25, 20, 10, 8, 5, 4, 2, 1

# c + b = a ** 2
# c - b = 1



# a ** 2 + a - 1000 = 0
# a ** 2 + a - 500 = 0
# a ** 2 + a - 250 = 0
# a ** 2 + a - 200 = 0
# a ** 2 + a - 125 = 0
# a ** 2 + a - 100 = 0
# a ** 2 + a - 50 = 0
# a ** 2 + a - 40 = 0
# a ** 2 + a - 25 = 0
# a ** 2 + a - 20 = 0  -4
# a ** 2 + a - 10 = 0
# a ** 2 + a - 8 = 0
# a ** 2 + a - 5 = 0
# a ** 2 + a - 4 = 0
# a ** 2 + a - 2 = 0  1
# a ** 2 + a - 1 = 0

# (a + 5)(a - 4) = 0
# a = 4

# o e  o o
# o o  e e
# e e  e e
# e o  o o

# 3 4 5
# 5 7 25 49  6 7


# c - b = 1
# a ** 2 = c + b

# a + b + c = 1000

# # 233168

# 3 4 5
# 5 12 13
# 7 24 25
# 9 40 41
# 11 60 61
# 13 84 85

# 3H1000 1002C1000    1002! / 2! / 1000! = 1001 * 501
