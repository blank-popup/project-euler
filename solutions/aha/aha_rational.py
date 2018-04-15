# -*- coding: utf-8 -*-
"""Module for rational number"""


import fractions

from . import aha_base as abase


logger = abase.get_logger(f'{abase.k_name_header}.{__name__}')


Fraction = fractions.Fraction


def get_farey_sequence(N):
    """Get farey sequence
    N: maximum of denominator
    return list of tuple(numerator, denominator)
    in case of N = 4
    [(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)]

    a   c   p
    - , - , -
    b   d   q

    # b * c - a * d = 1
    # d * p - c * q = 1

    a + p   c
    ----- = -
    b + q   d

    p = k * c - a < N                 N + b
    q = k * d - b <= N     <=>   k <= -----
                                      d"""

    farey = [(0, 1), (1, N)]
    while farey[-1][0] != 1 or farey[-1][1] != 1:
        k = (N + farey[-2][1]) // farey[-1][1]
        p = k * farey[-1][0] - farey[-2][0]
        q = k * farey[-1][1] - farey[-2][1]
        farey.append((p, q))
    return farey
