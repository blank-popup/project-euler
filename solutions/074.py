# -*- coding: utf-8 -*-


# 402
# take a long time


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    samples = [aint.factorial(ii) for ii in range(0, 10)]
    solutions = []
    for ii in range(3, 1000000):
        sequence = [ii]
        while True:
            digits = aint.get_digits(sequence[-1])
            sum_offactorial = sum([samples[digit] for digit in digits])
            if sum_offactorial in sequence:
                if len(sequence) == 60:
                    solutions.append(ii)
                if ii % 100000 == 0:
                    logger.info(f'{ii} : {len(sequence)}')
                break
            sequence.append(sum_offactorial)
    logger.info(len(solutions))

if __name__ == '__main__':
    main()
