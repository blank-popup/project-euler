# -*- coding: utf-8 -*-
"""Module for real number"""


import decimal
import dataclasses

from . import aha_base as abase
from . import aha_integer as aint


logger = abase.get_logger(f'{abase.k_name_header}.{__name__}')


@dataclasses.dataclass
class CF:
    """Class for continued fraction
    value =             1
            a0 + -----------------
                          1
                 a1 + ------------
                              1
                      a2 + -------
                           ...
    sequence: list of a0, a1, a2, ...
    repetend_length: length of repetend in sequence
    in case of sequenc = [1, 1, 2] repetend_length = 2
    a0 = 1, a1 = 1, a2 = 2, a3 = 1, a4 = 2, ...
    value_squared: value ** 2
    value_name: unique name for value
    numerator: numerator
    denominator: denominator"""
    sequence: list
    repetend_length: int = None
    value_squared: int = None
    value_name: str = None
    numerator: int = None
    denominator: int = None
    count_digit: int = None
    error: float = None

def make_continued_fraction_from_root(N):
    """Get CF(continued fraction)
    N: integer
    return: CF
    en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend
    064_mariusjp.pdf 064_alexajp.pdf

    N ** 0.5 + m
    ------------
    d

               N ** 0.5 + 0          1
    N ** 0.5 = ------------ = a(0) + -----------------
               1                      N ** 0.5 + a(0)
                                      ---------------
                                      N - a(0) ** 2


    m(0) = 0, d(0) = 1, a(0) = [N ** 0.5]
    m(1) = a(0), d(1) = N - a(0) ** 2
    m(n+1) = d(n) * a(n) - m(n)
    d(n+1) = (N - m(n+1) ** 2) / d(n)
    a(n+1) = [(a(0) + m(n+1)) / d(n+1)]
    terminate on a(k) when a(k) == 2 * a(0)"""

    if aint.is_square(N):
        return CF(sequence=[N], repetend_length=0, value_squared=N, numerator=N, denominator=1, count_digit=1, error=0)

    m = [0]
    d = [1]
    a = [int(N ** 0.5)]
    while a[-1] != 2 * a[0]:
        m.append(d[-1] * a[-1] - m[-1])
        d.append((N - m[-1] ** 2) // d[-1])
        a.append((a[0] + m[-1]) // d[-1])
    rl = len(a) - 1
    return CF(sequence=a, repetend_length=rl, value_squared=N)

def set_property_continued_fraction(Cf, Error, Length):
    """Set error and length in CF
    Cf: CF continued fraction
    Error: error
    Length: length
    return: None

    a(0)  a(1) * a(0) + 1  a(2) * (a(1) * a(0) + 1) + a(0)  a(3) * (a(2) * (a(1) * a(0) + 1) + a(0)) + (a(1) * a(0) + 1)
    ----, ---------------, -------------------------------, ------------------------------------------------------------
    1     a(1)             a(2) * a(1) + 1                  a(3) * (a(2) * a(1) + 1) + (a(1))

           numerator(n)     numerator(n-1) * a(n) + numerator(n-2)
    F(n) = -------------- = ------------------------------------------
           denominator(n)   denominator(n-1) * a(n) + denominator(n-2)

    numerators = [0, 1]
    denominators = [1, 0]"""

    def get_an(k):
        if k < len(Cf.sequence):
            return Cf.sequence[k]
        if CF.repetend_length is not None and CF.repetend_length < len(CF.sequence):
            return Cf.sequence[len(Cf.sequence) - Cf.repetend_length + (k + len(Cf.sequence) - Cf.repetend_length) % Cf.repetend_length]
        raise Exception('Invalid Continued Fraction: Cannot find an')

    numerators = [0, 1]
    denominators = [1, 0]
    k = 0
    while Error * denominators[-1] ** 2 < 1 and k < Length:
        an = get_an(k)
        numerators.append(numerators[-1] * an + numerators[-2])
        denominators.append(denominators[-1] * an + denominators[-2])
        k += 1

    Cf.numerator = numerators[-1]
    Cf.denominator = denominators[-1]
    Cf.count_digit = k
    Cf.error = 1 / denominators[-1] ** 2

def make_continued_fraction_from_root_0(N):
    """
    aa                                    aa * (bb * root_N - cc) (# 02 remain)
    ----------------------------------- = -------------------------------------
    bb * root_N + cc (# 01 denominator)   bb ** 2 * N - cc ** 2

                      aa * bb * root_N - aa * cc - dd * bb ** 2 * N + dd * cc ** 2
    = dd (# 03 ndd) + ------------------------------------------------------------
                      bb ** 2 * N - cc ** 2

    reverse
    bb ** 2 * N - cc ** 2 (# 04 naa)
    ----------------------------------------------------------------------------------
    aa * bb * root_N (# 05 nbb) - aa * cc - dd * bb ** 2 * N + dd * cc ** 2 (# 06 ncc)
    """

    if aint.is_square(N):
        return CF(sequence=[N], repetend_length=0, value_squared=N, numerator=N, denominator=1, count_digit=1, error=0)

    root_N = N ** 0.5
    n = int(root_N)

    dds = [n]
    aas = [1]
    bbs = [1]
    ccs = [-n]

    while True:
        denominator = bbs[-1] ** 2 * N - ccs[-1] ** 2 # 01 denominator
        remain = aas[-1] * (bbs[-1] * root_N - ccs[-1]) # 02 remain
        ndd = 0 # 03 ndd
        while remain >= denominator:
            remain -= denominator
            ndd += 1
        naa = bbs[-1] ** 2 * N - ccs[-1] ** 2 # 04 naa
        nbb = aas[-1] * bbs[-1] # 05 nbb
        ncc = - aas[-1] * ccs[-1] - ndd * bbs[-1] ** 2 * N + ndd * ccs[-1] ** 2 # 06 ncc
        if naa % nbb != 0:
            raise Exception(f'Strange result!!! - (naa % nbb): {naa} % {nbb}')
        if ncc % nbb != 0:
            raise Exception(f'Strange result!!! - (ncc % nbb): {ncc} % {nbb}')
        naa //= nbb
        ncc //= nbb
        nbb = 1
        for jj, _ in enumerate(dds):
            if dds[jj] == ndd and aas[jj] == naa and bbs[jj] == nbb and ccs[jj] == ncc:
                rl = len(dds) - jj
                return CF(sequence=dds, repetend_length=rl, value_squared=N)
        dds.append(ndd)
        aas.append(naa)
        bbs.append(nbb)
        ccs.append(ncc)

def set_property_continued_fraction_0(Cf, Error, Length):
    """
           C(n) * a(n) + D(n)                     1        a(n) * a(n+1) + 1
    F(n) = ------------------   substitute a(n) + ------ = ----------------- instead of a(n)
           A(n) * a(n) + B(n)                     a(n+1)   a(n+1)
             (C(n) * a(n) + D(n)) * a(n+1) + C(n)
    F(n+1) = ------------------------------------
             (A(n) * a(n) + B(n)) * a(n+1) + A(n)
    A(n+1) = A(n) * a(n) + B(n)
    B(n+1) = A(n)
    C(n+1) = C(n) * a(n) + D(n)
    D(n+1) = C(n)
    """

    def get_an(k):
        if k < len(Cf.sequence):
            return Cf.sequence[k]
        if CF.repetend_length is not None and CF.repetend_length < len(CF.sequence):
            return Cf.sequence[len(Cf.sequence) - Cf.repetend_length + (k + len(Cf.sequence) - Cf.repetend_length) % Cf.repetend_length]
        raise Exception('Invalid Continued Fraction: Cannot find an')

    aas = [1]
    bbs = [0]
    ccs = [0]
    dds = [1]
    denominator = Cf.sequence[1]
    numerator = Cf.sequence[0] * Cf.sequence[1] + 1
    k = 0
    while Error * denominator ** 2 < 1 and k + 2 < Length:
        k += 1
        an = get_an(k)
        aa = aas[-1] * an + bbs[-1]
        bb = aas[-1]
        cc = ccs[-1] * an + dds[-1]
        dd = ccs[-1]
        am = get_an(k + 1)
        denominator = aa * am + bb
        numerator = Cf.sequence[0] * denominator + cc * am + dd
        aas.append(aa)
        bbs.append(bb)
        ccs.append(cc)
        dds.append(dd)
    Cf.numerator = numerator
    Cf.denominator = denominator
    Cf.count_digit = k + 2
    Cf.error = 1 / denominator ** 2

def get_transcendental_continued_fraction(Name):
    """Get transcendental continued fraction
    Name: special name('pi', 'e')"""
    transcendentals = {
        'pi': [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1],
        'e': [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 60, 1, 1, 62, 1, 1, 64, 1, 1, 66],
    }
    if Name in transcendentals:
        return CF(sequence=transcendentals[Name], value_name=Name)
    else:
        return None


def calculate_pi_0(N):
    """Calculate PI"""
    decimal.getcontext().prec = 300
    side = decimal.Decimal('1')
    for ii in range(0, N):
        polygon = decimal.Decimal(str(6 * 2 ** ii))
        pi = polygon * side / decimal.Decimal('2')
        side = (decimal.Decimal('2') - (decimal.Decimal('4') - side ** decimal.Decimal('2')) ** decimal.Decimal('0.5')) ** decimal.Decimal('0.5')
    return pi
