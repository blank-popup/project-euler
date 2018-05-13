# -*- coding: utf-8 -*-


# 6531031914842725


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    numbers = list(ii for ii in range(1, 11))
    solutions = []

    ii0s = list(ii for ii in range(1, 7))
    for ii0 in ii0s:
        ii1s = numbers[:]
        ii1s.remove(ii0)
        for ii1 in ii1s:
            if ii1 == 10:
                continue
            ii2s = ii1s[:]
            ii2s.remove(ii1)
            for ii2 in ii2s:
                if ii2 == 10:
                    continue
                gon = ii0 + ii1 + ii2
                if gon < 14 or gon > 19:
                    continue
                ii3s = ii2s[:]
                ii3s.remove(ii2)
                for ii3 in ii3s:
                    if ii3 < ii0:
                        continue
                    ii4s = ii3s[:]
                    ii4s.remove(ii3)
                    for ii4 in ii4s:
                        if ii4 == 10:
                            continue
                        if ii3 + ii2 + ii4 != gon:
                            continue
                        ii5s = ii4s[:]
                        ii5s.remove(ii4)
                        for ii5 in ii5s:
                            if ii5 < ii0:
                                continue
                            ii6s = ii5s[:]
                            ii6s.remove(ii5)
                            for ii6 in ii6s:
                                if ii6 == 10:
                                    continue
                                if ii5 + ii4 + ii6 != gon:
                                    continue
                                ii7s = ii6s[:]
                                ii7s.remove(ii6)
                                for ii7 in ii7s:
                                    if ii7 < ii0:
                                        continue
                                    ii8s = ii7s[:]
                                    ii8s.remove(ii7)
                                    for ii8 in ii8s:
                                        if ii8 == 10:
                                            continue
                                        if ii7 + ii6 + ii8 != gon:
                                            continue
                                        ii9s = ii8s[:]
                                        ii9s.remove(ii8)
                                        for ii9 in ii9s:
                                            if ii9 < ii0:
                                                continue
                                            if ii9 + ii8 + ii1 != gon:
                                                continue
                                            solution = f'{ii0}{ii1}{ii2}{ii3}{ii2}{ii4}{ii5}{ii4}{ii6}{ii7}{ii6}{ii8}{ii9}{ii8}{ii1}'
                                            solutions.append(solution)
                                            logger.info(f'{ii0} {ii1} {ii2} {ii3} {ii4} {ii5} {ii6} {ii7} {ii8} {ii9}')
    for solution in solutions:
        logger.info(solution)
    solutions.sort()
    for solution in solutions:
        logger.info(solution)


if __name__ == '__main__':
    main()
