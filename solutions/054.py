# -*- coding: utf-8 -*-


# 376


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

def sort_cards(Player):
    cards = [[p[0], p[1]] for p in Player]
    for card in cards:
        if card[0] == 'A':
            card[0] = 1
        elif card[0] == 'T':
            card[0] = 10
        elif card[0] == 'J':
            card[0] = 11
        elif card[0] == 'Q':
            card[0] = 12
        elif card[0] == 'K':
            card[0] = 13
        else:
            card[0] = int(card[0])
    cards.sort(key=lambda x: x[0])
    return cards

def is_royal_flush(Cards):
    if Cards[0][0] == 1 and Cards[1][0] == 10 and Cards[2][0] == 11 and Cards[3][0] == 12 and Cards[4][0] == 13:
        if Cards[0][1] == Cards[1][1] == Cards[2][1] == Cards[3][1] == Cards[4][1]:
            return True
    return False

def is_straight_flush(Cards):
    if Cards[0][0] + 4 == Cards[1][0] + 3 == Cards[2][0] + 2 == Cards[3][0] + 1 == Cards[4][0]:
        if Cards[0][1] == Cards[1][1] == Cards[2][1] == Cards[3][1] == Cards[4][1]:
            return True
    return False

def is_four_of_a_kind(Cards):
    if Cards[0][0] == Cards[1][0] == Cards[2][0] == Cards[3][0] or Cards[1][0] == Cards[2][0] == Cards[3][0] == Cards[4][0]:
        return True
    return False

def is_full_house(Cards):
    if Cards[0][0] == Cards[1][0] == Cards[2][0] and Cards[3][0] == Cards[4][0] or Cards[0][0] == Cards[1][0] and Cards[2][0] == Cards[3][0] == Cards[4][0]:
        return True
    return False

def is_flush(Cards):
    if Cards[0][1] == Cards[1][1] == Cards[2][1] == Cards[3][1] == Cards[4][1]:
        return True
    return False

def is_straight(Cards):
    if Cards[0][0] + 4 == Cards[1][0] + 3 == Cards[2][0] + 2 == Cards[3][0] + 1 == Cards[4][0]:
        return True
    return False

def is_three_of_a_kind(Cards):
    if Cards[0][0] == Cards[1][0] == Cards[2][0] or Cards[1][0] == Cards[2][0] == Cards[3][0] or Cards[2][0] == Cards[3][0] == Cards[4][0]:
        return True
    return False

def is_two_pairs(Cards):
    if Cards[0][0] == Cards[1][0] and Cards[2][0] == Cards[3][0] or Cards[0][0] == Cards[1][0] and Cards[3][0] == Cards[4][0] or Cards[1][0] == Cards[2][0] and Cards[3][0] == Cards[4][0]:
        return True
    return False

def is_one_pair(Cards):
    if Cards[0][0] == Cards[1][0] or Cards[1][0] == Cards[2][0] or Cards[2][0] == Cards[3][0] or Cards[3][0] == Cards[4][0]:
        return True
    return False

def get_rank(Cards):
    if Cards[0][0] == 1 and Cards[1][0] == 10 and Cards[2][0] == 11 and Cards[3][0] == 12 and Cards[4][0] == 13 \
        and Cards[0][1] == Cards[1][1] == Cards[2][1] == Cards[3][1] == Cards[4][1]:
        rank = (10, (), Cards)
    elif Cards[0][0] + 4 == Cards[1][0] + 3 == Cards[2][0] + 2 == Cards[3][0] + 1 == Cards[4][0] \
        and Cards[0][1] == Cards[1][1] == Cards[2][1] == Cards[3][1] == Cards[4][1]:
        rank = (9, (), Cards)
    elif Cards[0][0] == Cards[1][0] == Cards[2][0] == Cards[3][0]:
        rank = (8, (Cards[3][0],), Cards)
    elif Cards[1][0] == Cards[2][0] == Cards[3][0] == Cards[4][0]:
        rank = (8, (Cards[4][0],), Cards)
    elif Cards[0][0] == Cards[1][0] == Cards[2][0] and Cards[3][0] == Cards[4][0]:
        rank = (7, (Cards[2][0], Cards[4][0]), Cards)
    elif Cards[0][0] == Cards[1][0] and Cards[2][0] == Cards[3][0] == Cards[4][0]:
        rank = (7, (Cards[4][0], Cards[2][0]), Cards)
    elif Cards[0][1] == Cards[1][1] == Cards[2][1] == Cards[3][1] == Cards[4][1]:
        rank = (6, (), Cards)
    elif Cards[0][0] + 4 == Cards[1][0] + 3 == Cards[2][0] + 2 == Cards[3][0] + 1 == Cards[4][0]:
        rank = (5, (), Cards)
    elif Cards[0][0] == Cards[1][0] == Cards[2][0]:
        rank = (4, (Cards[2][0],), Cards)
    elif Cards[1][0] == Cards[2][0] == Cards[3][0]:
        rank = (4, (Cards[3][0],), Cards)
    elif Cards[2][0] == Cards[3][0] == Cards[4][0]:
        rank = (4, (Cards[4][0],), Cards)
    elif Cards[0][0] == Cards[1][0] and Cards[2][0] == Cards[3][0]:
        if Cards[0][0] == 1:
            rank = (3, (Cards[0][0], Cards[3][0]), Cards)
        else:
            rank = (3, (Cards[3][0], Cards[1][0]), Cards)
    elif Cards[0][0] == Cards[1][0] and Cards[3][0] == Cards[4][0]:
        if Cards[0][0] == 1:
            rank = (3, (Cards[0][0], Cards[4][0]), Cards)
        else:
            rank = (3, (Cards[4][0], Cards[1][0]), Cards)
    elif Cards[1][0] == Cards[2][0] and Cards[3][0] == Cards[4][0]:
        rank = (3, (Cards[4][0], Cards[2][0]), Cards)
    elif Cards[0][0] == Cards[1][0]:
        rank = (2, (Cards[1][0],), Cards)
    elif Cards[1][0] == Cards[2][0]:
        rank = (2, (Cards[2][0],), Cards)
    elif Cards[2][0] == Cards[3][0]:
        rank = (2, (Cards[3][0],), Cards)
    elif Cards[3][0] == Cards[4][0]:
        rank = (2, (Cards[4][0],), Cards)
    else:
        rank = (1, (), Cards)
    return rank

def who_is_winner(Rank1, Rank2):
    if Rank1[0] > Rank2[0]:
        return 1
    if Rank1[0] < Rank2[0]:
        return 2
    for c in range(0, len(Rank1[1])):
        if Rank1[1][c] == 1 and Rank2[1][c] != 1:
            return 1
        if Rank1[1][c] != 1 and Rank2[1][c] == 1:
            return 2
        if Rank1[1][c] > Rank2[1][c]:
            return 1
        if Rank1[1][c] < Rank2[1][c]:
            return 2
    if Rank1[2][0][0] == 1 and Rank2[2][0][0] != 1:
        return 1
    if Rank1[2][0][0] != 1 and Rank2[2][0][0] == 1:
        return 2
    for c in range(4, -1, -1):
        if Rank1[2][c][0] > Rank2[2][c][0]:
            return 1
        if Rank1[2][c][0] < Rank2[2][c][0]:
            return 2
    return 0

@abase.tick(logger)
def main():
    solutions = {0: 0, 1: 0, 2: 0}
    data = abase.read_file(abase.dirpath_problems + '/p054_poker.txt')
    games = data.split('\n')
    for game in games:
        if game.strip() == '':
            continue
        cards = game.split(' ')
        player1 = cards[0:5]
        player2 = cards[5:10]
        rank1 = get_rank(sort_cards(player1))
        rank2 = get_rank(sort_cards(player2))
        solutions[who_is_winner(rank1, rank2)] += 1
    logger.info(solutions)

if __name__ == '__main__':
    main()
