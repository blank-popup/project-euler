# -*- coding: utf-8 -*-


# 837799


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')


def get_next_term(N):
    if N % 2 == 0:
        return int(N / 2)
    return 3 * N + 1


@abase.tick(logger)
def main():
    solutions = {}

    for sn in range(1, 1000000):
        terms = [sn]
        while True:
            if terms[-1] in solutions:
                terms += solutions[terms[-1]][1:]
            else:
                terms.append(get_next_term(terms[-1]))
            if terms[-1] == 1:
                break
        solutions[sn] = terms

    solutions = [(k, terms) for k, terms in solutions.items()]
    solutions.sort(key=lambda x: len(x[1]), reverse=True)
    logger.info(solutions[0])


if __name__ == '__main__':
    main()
