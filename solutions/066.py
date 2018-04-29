# -*- coding: utf-8 -*-


# 661
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

# https://radiusofcircle.blogspot.com/2017/01/project-euler-problem-66-solution-with-python.html
# The solution is based on two approaches: Chakravala method(066_chakravala.pdf)(Page No:3) and Continued Fraction method(066_unger_2009_report.pdf)(Page No: 18). And to find continued fractions I have used this source: Wikipedia - Methods of Computing square roots.
# 1. If the period of the continued fraction is even then we are finding the solution for the positive pells equation - $ x^{2} - Dy^{2} = 1 $
# 2. If the period of the continued fraction is odd then we are finding the solution for the negative pells equation - $ x^{2} - Dy^{2} = -1 $
# 3. What ever might be the case, we don't need the last value of the convergent list. i.e. in our case $ \sqrt{19} = [4;2,1,3,1,2] $ instead of $ [4;2,1,3,1,2,8] $
# 4. If we are solving the negative pells equation, then we will use Baskara's Lemma to get the required answer.
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
    # variable to store the largest value
    # and the place it occurs
    largest = 0, 0

    # for loop less than 1000
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

    # print the largest value
    logger.info(largest)

if __name__ == '__main__':
    main()


# @abase.tick(logger)
# def main():
#     solutions = []
#     for D in range(661, 662):
#         if aint.is_square(D):
#             continue
#         y = 1
#         while True:
#             x_square = 1 + D * y ** 2
#             if aint.is_square(x_square):
#                 solutions.append((D, int(x_square ** 0.5), y))
#                 break
#             y += 1
#         logger.info(f'Checked {D} {solutions[-1]}')
#     solutions.sort(key=lambda x: x[1])
#     for solution in solutions:
#         logger.info(solution)

# if __name__ == '__main__':
#     main()
