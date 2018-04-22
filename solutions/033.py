# -*- coding: utf-8 -*-


# 100

# (a * 10 + c) / (a * 10 + b) = c / b
# (c * 10 + a) / (b * 10 + a) = c / b
# (a * 10 + c) / (b * 10 + a) = c / b
# (c * 10 + a) / (a * 10 + b) = c / b


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    solutions = []
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, b):
                if (a * 10 + c) * b == (a * 10 + b) * c:
                    solutions.append((0, a, b, c))
                if (c * 10 + a) * b == (b * 10 + a) * c:
                    solutions.append((1, a, b, c))
                if (a * 10 + c) * b == (b * 10 + a) * c:
                    solutions.append((2, a, b, c))
                if (c * 10 + a) * b == (a * 10 + b) * c:
                    solutions.append((3, a, b, c))

    logger.info(solutions)
    product_numerator = 1
    product_denominator = 1
    for s in solutions:
        product_numerator *= s[3]
        product_denominator *= s[2]
        cd = aint.gcd(product_numerator, product_denominator)
        product_numerator //= cd
        product_denominator //= cd
    logger.info(product_denominator)

if __name__ == '__main__':
    main()
