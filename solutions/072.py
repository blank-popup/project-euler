# -*- coding: utf-8 -*-


# 303963552391


from aha import aha_base as abase
from aha import aha_integer as aint

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def count_multiple_of_number(Bound, M):
    count = 0
    for ii in range(M, Bound + 1, M):
        count += aint.count_multiples(Bound + 1, M) - aint.count_multiples(ii, M)
    return count


@abase.tick(logger)
def main():
    bound_up = 1000000
    solutions = [int((bound_up - 1) * bound_up / 2)]
    primes = aint.collect_prime_numbers(bound_up + 1)

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    for ii1 in range(0, len(primes)):
        count1 += count_multiple_of_number(bound_up, primes[ii1])
        for ii2 in range(ii1 + 1, len(primes)):
            product2 = primes[ii1] * primes[ii2]
            if product2 > bound_up:
                break
            count2 += count_multiple_of_number(bound_up, product2)
            for ii3 in range(ii2 + 1, len(primes)):
                product3 = primes[ii1] * primes[ii2] * primes[ii3]
                if product3 > bound_up:
                    break
                count3 += count_multiple_of_number(bound_up, product3)
                for ii4 in range(ii3 + 1, len(primes)):
                    product4 = primes[ii1] * primes[ii2] * primes[ii3] * primes[ii4]
                    if product4 > bound_up:
                        break
                    count4 += count_multiple_of_number(bound_up, product4)
                    for ii5 in range(ii4 + 1, len(primes)):
                        product5 = primes[ii1] * primes[ii2] * primes[ii3] * primes[ii4] * primes[ii5]
                        if product5 > bound_up:
                            break
                        count5 += count_multiple_of_number(bound_up, product5)
                        for ii6 in range(ii5 + 1, len(primes)):
                            product6 = primes[ii1] * primes[ii2] * primes[ii3] * primes[ii4] * primes[ii5] * primes[ii6]
                            if product6 > bound_up:
                                break
                            count6 += count_multiple_of_number(bound_up, product6)
                            for ii7 in range(ii6 + 1, len(primes)):
                                product7 = primes[ii1] * primes[ii2] * primes[ii3] * primes[ii4] * primes[ii5] * primes[ii6] * primes[ii7]
                                if product7 > bound_up:
                                    break
                                count7 += count_multiple_of_number(bound_up, product7)
    solutions.append(-count1)
    solutions.append(count2)
    solutions.append(-count3)
    solutions.append(count4)
    solutions.append(-count5)
    solutions.append(count6)
    solutions.append(-count7)
    logger.info(solutions)
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
