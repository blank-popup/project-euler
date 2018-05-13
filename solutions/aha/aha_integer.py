# -*- coding: utf-8 -*-
"""Module for calculation of integer

augend + addend = sum
summand + addend = sum
addend + addend = sum
minuend - subtrahend = difference
multiplicand * multiplier = product
dividend / divisor = quotient ... remainder"""

import math
import itertools

from . import aha_base as abase


logger = abase.get_logger(f'{abase.k_name_header}.{__name__}')

def collect_prime_numbers(N):
    """Get list of prime number equal of less than N
    N: maximum integer getting prime number
    return: list of prime numbers"""
    def delete_composite_number(Prime):
        index = 2 * Prime
        while index < len(numbers):
            numbers[index] = 0
            index += Prime

    def find_next_prime(Prime):
        index = Prime + 1
        while numbers[index] == 0:
            index += 1
        return numbers[index]

    root_n = N ** 0.5
    numbers = list(range(0, N + 1))

    prime = 2

    while prime <= root_n:
        delete_composite_number(prime)
        prime = find_next_prime(prime)

    return [numbers[ii] for ii in range(0, len(numbers)) if numbers[ii] != 0][1:]

PRIMES = collect_prime_numbers(1000000)

def is_prime_number(N):
    """Check if number is prime or not
    N: integer of checking
    return: True if N is prime number, otherwise False"""
    if N in PRIMES:
        return True
    if N <= PRIMES[-1]:
        return False
    root_n = int(N ** 0.5)
    for prime in PRIMES:
        if prime > root_n:
            return True
        if N % prime == 0:
            return False
    prime = PRIMES[-1] + 2
    while prime <= root_n:
        if N % prime == 0:
            return False
        prime += 2
    return True

def factorize(N):
    """Factorize number and return dictionary of result
    N: integer of factorizing
    return: dictionary of factors"""
    def insert_factor(divisor):
        if divisor in factors:
            factors[divisor] += 1
        else:
            factors[divisor] = 1
    number = N
    factors = {}
    index_divisor = 0
    divisor = PRIMES[index_divisor]
    while number > 1:
        if divisor > number ** 0.5:
            insert_factor(number)
            break
        if number % divisor == 0:
            insert_factor(divisor)
            number //= divisor
        else:
            if index_divisor < len(PRIMES) - 1:
                index_divisor += 1
                divisor = PRIMES[index_divisor]
            else:
                divisor += 2
    return factors

def count_divisor(Factors):
    """Get the number of divisor from dictionary of factor
    Factors: dictionary of factor
    return: the number of divisor"""
    count = 1
    for factor in Factors:
        count *= Factors[factor] + 1
    return count

def get_divisors(N):
    """Get all divisors of N
    N: integer
    return: list of divisors"""
    factors = factorize(N)
    fs = []
    for factor, _ in factors.items():
        for f in range(0, factors[factor]):
            fs.append(factor)
    divisors = []
    for ii in range(0, len(fs) + 1):
        cs = combinations(fs, ii)
        for c in cs:
            divisor = 1
            for f in c:
                divisor *= f
            divisors.append(divisor)
    divisors.append(N)
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

def get_greatest_common_divisor(*Ns):
    """Get greatest common divisor
    Ns: tuple of integers
    return: greatest common divisor of Ns"""
    def get_cd(a, b):
        if a > b:
            a, b = b, a
        while b > 0:
            a, b = b, a % b
        return a
    a = Ns[0]
    for ii in range(1, len(Ns)):
        a = get_cd(a, Ns[ii])
    return a

def get_leatest_common_multiple(*Ns):
    """Get leatest common multiple
    Ns: tuple of integers
    return: leatest common multiple of Ns"""
    a = Ns[0]
    for ii in range(1, len(Ns)):
        cd = get_greatest_common_divisor(a, Ns[ii])
        a = a * Ns[ii] // cd
    return a

def count_multiples(N, B):
    """Get the number of multiple
    N: max integer
    B: base
    return: the count of multiples of base in range(1, N + 1)"""
    return N // B


def get_euler_totient(N):
    """Get euler phi value"""
    if N in PRIMES:
        return N - 1
    factors = factorize(N)
    totient = 1
    for factor, count in factors.items():
        totient *= factor ** (count - 1) * (factor - 1)
    return totient


def factorial(N):
    """Get factorial
    N: integer
    return: factorial"""
    factiorial = 1
    for ii in range(2, N + 1):
        factiorial *= ii
    return factiorial

def meta_combinations(N, R):
    """Generate meta combination
    N: n of nCr
    R: r of nCr
    in case of N = 5 and R = 3
    yield: (0, 1, 2), (0, 1, 3), (0, 1, 4), ... , (2, 3, 4)"""
    def plus_one(current):
        k = R - 1
        while True:
            if current[k] == N - R + k:
                k -= 1
            else:
                break
        digit = current[k] + 1
        return tuple(current[ii] if ii < k else digit + ii - k for ii in range(0, R))
    current = tuple(range(0, R))
    last = tuple(range(N - R, N))
    yield current
    while current != last:
        current = plus_one(current)
        yield current

def meta_permutations(N, R):
    """ Generate meta permutation
    N: n of nPr
    R: r of nPr
    in case of N = 5 and R = 3
    yield: (0, 1, 2), (0, 1, 3), ... , (0, 4, 3), ... , (4, 3, 2)"""
    def plus_one(current):
        array = list(current)
        k = R - 1
        while True:
            used = array[:k]
            candidates = list(range(0, N))
            for u in used:
                candidates.remove(u)
            if max(candidates) <= array[k]:
                k -= 1
            else:
                break
        for ii in range(k, R):
            if ii == k:
                for c in candidates:
                    if c > array[ii]:
                        array[ii] = c
                        candidates.remove(array[ii])
                        break
            else:
                array[ii] = min(candidates)
                candidates.remove(array[ii])
        return tuple(array)
    current = tuple(range(0, R))
    last = tuple(range(N - 1, N - R - 1, -1))
    yield current
    while current != last:
        current = plus_one(current)
        yield current

def meta_combinations_with_repitition(N, R):
    """Generate meta combination with repitition
    N: n of nCRr
    R: r of nCRr
    in case of N = 5 and R = 3
    yield: (0, 0, 0), (0, 0, 1), (0, 0, 2), ... , (4, 4, 4)"""
    def plus_one(current):
        k = R - 1
        while True:
            if current[k] == N - 1:
                k -= 1
            else:
                break
        digit = current[k] + 1
        return tuple(current[ii] if ii < k else digit for ii in range(0, R))
    current = (0, ) * R
    last = (N - 1, ) * R
    yield current
    while current != last:
        current = plus_one(current)
        yield current
meta_combinations_r = meta_combinations_with_repitition

def meta_permutations_with_repitition(N, R):
    """Generate meta permutation with repitition
    N: n of nPRr
    R: r of nPRr
    in case of N = 5 and R = 3
    yield: (0, 0, 0), (0, 0, 1), ... , (2, 2, 1), ... , (4, 4, 4)"""
    def plus_one(current):
        k = R - 1
        while True:
            if current[k] == N - 1:
                k -= 1
            else:
                break
        return tuple(current[ii] if ii < k else (current[ii] + 1 if ii == k else 0) for ii in range(0, R))
    current = (0, ) * R
    last = (N - 1, ) * R
    yield current
    while current != last:
        current = plus_one(current)
        yield current
meta_permutations_r = meta_permutations_with_repitition

def apply_meta_to_array(Meta, Array):
    """Generate array applying meta to Array
    Meta: Generator of manipulating
    Array: list of manipulating object
    in case of Meta = (0, 1), (1, 2) and Array = ['A', 'B', 'C']
    yield: ['A', 'B'], ['B', 'C']"""
    for ms in Meta:
        s = []
        for m in ms:
            s.append(Array[m])
        yield s

def combinations(Array, R):
    """Generate combination of selecting R from among arrays
    Array: list of manipulating object
    R: the number of manipulating
    in case of Array = ['A', 'B', 'C', 'D'] and R = 2
    return: generator of (['A', 'B'], ['A', 'C'], ... , ['C', 'D'])"""
    meta = meta_combinations(len(Array), R)
    return apply_meta_to_array(meta, Array)

def permutations(Array, R):
    """Generate permutation of selecting R from among arrays
    Array: list of manipulating object
    R: the number of manipulating
    in case of Array = ['A', 'B', 'C', 'D'] and R = 2
    return: generator (['A', 'B'], ['A', 'C'], ... , ['B', 'A'], ... , ['D', 'C'])"""
    meta = meta_permutations(len(Array), R)
    return apply_meta_to_array(meta, Array)

def combinations_with_repitition(Array, R):
    """Generate combination with repitition of selecting R from among arrays
    Array: list of manipulating object
    R: the number of manipulating
    in case of Array = ['A', 'B', 'C', 'D'] and R = 2
    return: generator (['A', 'A'], ['A', 'B'], ... , ['B', 'B'], ... , ['D', 'D'])"""
    meta = meta_combinations_with_repitition(len(Array), R)
    return apply_meta_to_array(meta, Array)

def permutations_with_repitition(Array, R):
    """Genrate permutation with repitition of selecting R from among arrays
    Array: list of manipulating object
    R: the number of manipulating
    in case of Array = ['A', 'B', 'C', 'D'] and R = 2
    return: generator (['A', 'A'], ['A', 'B'], ... , ['B', 'A'], ... , ['D', 'D'])
    Using itertools.product, not pernutations_r(Array, R) but pernutations_r(Array, repeat=R)"""
    meta = meta_permutations_with_repitition(len(Array), R)
    return apply_meta_to_array(meta, Array)

def partitions(N, R=None):
    """Generate partition of natural number
    N: natural number
    R: the count of partition
    in case of N = 5 and R = None
    yield: (5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)
    in case of N = 5 and R = 3
    yield: (3, 1, 1), (2, 2, 1)"""
    def plus_one(current):
        k = len(current) - 1
        while True:
            if current[k] == 1:
                k -= 1
            else:
                break
        tail = current[k] - 1
        dividend = N - sum(current[0:k])
        count, remain = divmod(dividend, tail)
        if remain == 0:
            return tuple(current[0:k] + (tail,) * count)
        return tuple(current[0:k] + (tail,) * count + (remain,))
    current = tuple([N])
    last = tuple([1] * N)
    if R is None:
        yield current
        while current != last:
            current = plus_one(current)
            yield current
    else:
        if len(current) == R:
            yield current
        while current != last:
            current = plus_one(current)
            if len(current) == R:
                yield current

def get_table_second_stirling(N, Table=None):
    """Get the table of stirling numbers of the second kind
    N: natural number
    Table: the table of stirling numbers of the second kind
    return: table(list of list)

    S(n, 1) = 1
    S(n, n) = 1
    S(n, k) = S(n - 1, k - 1) + k * P(n - 1, k)

    jj: n
    ii: k
    in case of N = 9
           jj = 1   jj = 2   jj = 3   jj = 4   jj = 5   jj = 6   jj = 7   jj = 8   jj = 9
    ii = 1    1        1        1        1        1        1        1        1        1
    ii = 2             1        3        7       15       31       63      127      255
    ii = 3                      1        6       25       90      301      966     3025
    ii = 4                               1       10       65      350     1701     7770
    ii = 5                                        1       15      140     1050     6951
    ii = 6                                                 1       21      266     2646
    ii = 7                                                          1       28      462
    ii = 8                                                                   1       36
    ii = 9                                                                            1"""

    if Table == None:
        table = []
    else:
        table = Table

    constraints = [c for c in range(1, N + 1)]
    for ii, constraint in enumerate(constraints):
        if constraint > N:
            break
        if ii >= len(table):
            table.append([])
        for jj, JJ in enumerate(range(1, N + 1)):
            if jj < len(table[ii]):
                continue
            if ii == 0:
                table[ii].append(1)
            else:
                if JJ < constraint:
                    table[ii].append(0)
                elif JJ == constraint:
                    table[ii].append(1)
                else:
                    table[ii].append(table[ii - 1][jj - 1] + constraint * table[ii][jj - 1])
    return table

def get_table_partitions(N, Table=None):
    """Get the table of partitions
    N: natural number
    Table: the table of partition
    return: table(list of list)

    P(n, 1) = 1
    P(n, n) = 1
    P(n) = P(n, 1) + P(n, 2) + ... + P(n, n)
    P(n, k) = P(n - k, 1) + P(n - k, 2) + ... + P(n - k, k)
    P(n, k) = P(n - 1, k - 1) + P(n - k, k)

    jj: n
    ii: k
    in case of N = 9
           jj = 1   jj = 2   jj = 3   jj = 4   jj = 5   jj = 6   jj = 7   jj = 8   jj = 9
    ii = 1    1        1        1        1        1        1        1        1        1
    ii = 2             1        1        2        2        3        3        4        4
    ii = 3                      1        1        2        3        4        5        7
    ii = 4                               1        1        2        3        5        6
    ii = 5                                        1        1        2        3        5
    ii = 6                                                 1        1        2        3
    ii = 7                                                          1        1        2
    ii = 8                                                                   1        1
    ii = 9                                                                            1"""

    return get_table_way_sums_of_constraints(N, [c for c in range(1, N + 1)], Table)

def get_digits(N):
    """Get list all digits"""
    return [int(s) for s in str(N)]

def sum_of_digit(N):
    """Get sum of all digits"""
    return sum(get_digits(N))

def count_digits(N):
    """Get the number of all digits"""
    return len(get_digits(N))


def floor(R):
    """Round down"""
    if R >= 0:
        return int(R)
    return int(R) - 1

def ceil(R):
    """Round up"""
    n = floor(R)
    if n == R:
        return n
    return n + 1

def is_square(R):
    """Check if R is a square number or not"""
    return int(R ** 0.5) ** 2 == R


if abase.USE_PYTHON_MODULE:
    gcd = math.gcd
    lcm = math.lcm
    factorial = math.factorial
    combinations = itertools.combinations
    permutations = itertools.permutations
    combinations_r = itertools.combinations_with_replacement
    permutations_r = itertools.product
    floor = math.floor
    ceil = math.ceil
else:
    gcd = get_greatest_common_divisor
    lcm = get_leatest_common_multiple
    combinations_r = combinations_with_repitition
    permutations_r = permutations_with_repitition


def get_rotations(Array):
    """Get list of rotations
    Array: list
    return: rotations
    in case of Array = [1, 2, 3]
    return: [[1, 2, 3], [2, 3, 1], [3, 1, 2]"""
    rotations = []
    rotations.append(Array)
    while True:
        nr = rotations[-1][1:] +[rotations[-1][0]]
        if rotations[0] == nr:
            break
        rotations.append(nr)
    return rotations


def get_value_base(Notation, Base):
    """Get value converted notation in base to decimal
    Notation: number written in string
    Base: base
    return: number in decimal"""
    notation = Notation.upper()
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    values = {value: ii for ii, value in enumerate(digits)}
    value = sum([values[s] * (Base ** (len(notation) - ii - 1)) for ii, s in enumerate(notation)])
    return value


def get_notation_base(Value, Base):
    """Get notation converted value in decimal to base
    Value: number in decimal
    Base: base
    return: number in base written in string"""
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    notation = ''
    q = Value
    while q > 0:
        q, r = divmod(q, Base)
        notation += digits[r]
    return notation[::-1]


def convert_base(Notation, ToBase, FromBase):
    """Get natation converted FromBase to ToBase
    Notation: number written in string
    ToBase: base before converting
    FromBase: base after converting
    return: notation converted"""
    value = get_value_base(Notation, FromBase)
    return get_notation_base(value, ToBase)


def generate_N_angle_number(N):
    """Generate N angle number
    N: the number of angle(3, 4, 5, ...)
    in case of N = 3
    yield: 1, 3, 6, ..."""
    k = 0
    N_angle_number = 0
    while True:
        increment = (N - 1) + (N - 2) * (k - 1)
        N_angle_number += increment
        yield N_angle_number
        k += 1

def get_table_way_sums_of_constraints(N, Constraints=PRIMES, Table=None):
    """Get table of way of sums of constraints
    N: integer
    Constraints: list of integer that is the element to be added, must be sorted and non-duplicate
    Table: list of list of integer that is the count of sum way with constraints
    return: table(list of list )
    in case of N = 10 and Constraints = [2, 3, 5, 7]
    return: following table with zero in empty cell
           jj = 1   jj = 2   jj = 3   jj = 4   jj = 5   jj = 6   jj = 7   jj = 8   jj = 9   jj = 10
    ii = 2    0        1        0        1        0        1        0        1        0        1
    ii = 3                      1        0        1        1        1        1        2        1
    ii = 5                                        1        0        1        1        1        2
    ii = 7                                                          1        0        1        1"""

    if Table == None:
        table = []
    else:
        table = Table

    constraints = Constraints
    for ii, constraint in enumerate(constraints):
        if constraint > N:
            break
        if ii >= len(table):
            table.append([])
        for jj, JJ in enumerate(range(1, N + 1)):
            if jj < len(table[ii]):
                continue
            if ii == 0:
                if JJ % constraint == 0:
                    table[ii].append(1)
                else:
                    table[ii].append(0)
            else:
                if JJ < constraint:
                    table[ii].append(0)
                elif JJ == constraint:
                    table[ii].append(1)
                else:
                    count = 0
                    for kk in range(0, ii + 1):
                        count += table[kk][jj - constraint]
                    table[ii].append(count)
    return table

def get_intersection(LS):
    """Get intersection of list of set
    LS: list of set
    return intersection"""
    length = len(LS)
    if length == 0:
        return set()
    intersection = LS[0]
    for ii in range(1, length):
        intersection = intersection & LS[ii]
    return intersection

def get_union(LS):
    """Get union of list of set
    LS: list of set
    return union"""
    length = len(LS)
    if length == 0:
        return set()
    union = LS[0]
    for ii in range(1, length):
        union = union & LS[ii]
    return union

def get_count_inclusionexclusion(LS):
    """Get case count using inclusionexclusion
    LS: list of set
    return: case count"""
    count = 0
    length = len(LS)
    for ii in range(1, length + 1):
        for sets in combinations(LS, ii):
            count += (-1) ** (ii + 1) * len(get_intersection(sets))
    return count
