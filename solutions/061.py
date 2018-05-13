# -*- coding: utf-8 -*-


# 28684


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def find_next(Solutions, Used, Numbers):
    if set(Used) == set(range(0, 6)):
        if Solutions[-1] % 100 == Solutions[0] // 100:
            logger.info(f'{str(Solutions)} {sum(Solutions)}')
        return
    for ii in range(0, 6):
        if ii in Used:
            continue
        for candidate in Numbers[ii]:
            if Solutions[-1] % 100 == candidate // 100:
                find_next(Solutions + [candidate], Used + [ii], Numbers)


@abase.tick(logger)
def main():
    numbers = []
    numbers.append([int(ii * (ii + 1) / 2) for ii in range(0, 200) if 1000 <= ii * (ii + 1) / 2 < 10000])
    numbers.append([int(ii * ii) for ii in range(0, 200) if 1000 <= ii * ii < 10000])
    numbers.append([int(ii * (3 * ii - 1) / 2) for ii in range(0, 200) if 1000 <= ii * (3 * ii - 1) / 2 < 10000])
    numbers.append([int(ii * (2 * ii - 1)) for ii in range(0, 200) if 1000 <= ii * (2 * ii - 1) < 10000])
    numbers.append([int(ii * (5 * ii - 3) / 2) for ii in range(0, 200) if 1000 <= ii * (5 * ii - 3) / 2 < 10000])
    numbers.append([int(ii * (3 * ii - 2)) for ii in range(0, 200) if 1000 <= ii * (3 * ii - 2) < 10000])

    for n in numbers[5]:
        find_next([n], [5], numbers)

if __name__ == '__main__':
    main()
