# -*- coding: utf-8 -*-


# 661
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(n ** 0.5)
    an = int(n ** 0.5)
    convergents = [a0]
    period = 0
    if a0 != n ** 0.5:
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

def cf_inv(cf):
    """
    function to calculate the
    simple fraction from the continued
    fraction.
    """
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator, numerator = denominator*cf.pop() + numerator, denominator
    return denominator, numerator

@abase.tick(logger)
def main():
    largest = 0, 0

    for i in range(1, 1001):
        if i % (i ** 0.5) != 0:
            continued_fraction = cf(i)
            if len(continued_fraction) % 2 != 0:
                u, v = cf_inv(continued_fraction)
                u, v = 2*u**2+1, 2*u*v
            else:
                u, v = cf_inv(continued_fraction)
            if u > largest[1]:
                largest = i, u
            logger.info((i, u, v))

    logger.info(largest)

if __name__ == '__main__':
    main()
