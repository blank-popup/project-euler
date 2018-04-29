# -*- coding: utf-8 -*-


# 129448


from aha import aha_base as abase

name_sub_logger = abase.get_filename_from_filepath(__file__).split('.')[0]
logger = abase.get_logger(f'{abase.k_name_header}.{name_sub_logger}')
abase.set_logger(logger, f'{name_sub_logger}.log')

@abase.tick(logger)
def main():
    data = abase.read_file(abase.dirpath_problems + '/p059_cipher.txt')
    ciphers = [int(c) for c in data.split(',')]
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                keys = [a, b, c]
                plains = [chr(keys[ii % 3] ^ cipher) for ii, cipher in enumerate(ciphers)]
                count_lower = sum([1 for plain in plains if 'a' <= plain <= 'z'])
                if count_lower / len(plains) > 0.7:
                    logger.info(f'[{chr(a)}{chr(b)}{chr(c)}] : {"".join(plains)}')

    keys = [ord('e'), ord('x'), ord('p')]
    plains = [chr(keys[ii % 3] ^ cipher) for ii, cipher in enumerate(ciphers)]
    solutions = [ord(plain) for plain in plains]
    logger.info(sum(solutions))

if __name__ == '__main__':
    main()
