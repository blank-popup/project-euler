# -*- coding: utf-8 -*-


# 127035954683


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def find_permutations(Solutions, Cubes, Length):
    if len(Cubes[Length - 1]) >= 5:
        for ii in range(0, len(Cubes[Length - 1]) - 4):
            value = aint.get_digits(Cubes[Length - 1][ii])
            value.sort()
            permutations = [Cubes[Length - 1][ii]]
            for jj in range(ii + 1, len(Cubes[Length - 1])):
                candidate = aint.get_digits(Cubes[Length - 1][jj])
                candidate.sort()
                if value == candidate:
                    permutations.append(Cubes[Length - 1][jj])
            if len(permutations) >= 5:
                logger.info(permutations)
                Solutions.append(permutations)
                break

@abase.tick(logger)
def main():
    cubes = {1: []}
    number = 1
    length = 1
    solutions = []
    while True:
        value = number ** 3
        length = aint.count_digits(value)
        if length in cubes:
            cubes[length].append(value)
        else:
            cubes[length] = [value]
            find_permutations(solutions, cubes, length)
            logger.info(f'Checked to {number - 1}')
        if len(solutions) > 0:
            break
        number += 1

if __name__ == '__main__':
    main()
