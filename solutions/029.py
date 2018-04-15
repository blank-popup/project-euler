# -*- coding: utf-8 -*-


# 9183


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')


def exist_a(A, Dict_abs):
    for a, bs in Dict_abs.items():
        for b in bs:
            if a ** b == A:
                return True
    return False

@abase.tick(logger)
def main():
    range_a = range(2, 101)
    range_b = range(2, 101)

    dict_abs = {}
    # dict_abs[2] = [1, 2, 3, 4, 5, 6]
    # dict_abs[3] = [1, 2, 3, 4]
    # dict_abs[5] = [1, 2]
    # dict_abs[6] = [1, 2]
    # dict_abs[7] = [1, 2]
    # dict_abs[10] = [1, 2]
    # dict_abs[11] = [1]
    # dict_abs[12] = [1]
    # ...
    # dict_abs[100] = [1]
    for a in range_a:
        if exist_a(a, dict_abs) == True:
            continue
        dict_abs[a] = [1]
        for b in range_b:
            if a ** b > max(range_a):
                break
            dict_abs[a].append(b)

    solution = 0
    for a, bs in dict_abs.items():
        ls = []
        for b in bs:
            ls.append({(a ** b) ** rb for rb in range_b})
        solution += aint.get_count_inclusionexclusion(ls)
    logger.info(solution)

    # solutions = []
    # for a in range(2, 101):
    #     for b in range(2, 101):
    #         solutions.append(a ** b)
    # solutions = list(set(solutions))
    # logger.info(len(solutions))

if __name__ == '__main__':
    main()
