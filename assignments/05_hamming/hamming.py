#!/usr/bin/env python3
"""
Author : CeciliaChow
Date   : 2020-02-29
Purpose: hamming.py
"""

import argparse
import sys
import os
import itertools


# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming Distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-m',
                        '--min',
                        metavar='int',
                        type=int,
                        default=0,
                        help='minimum integer value')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    while True:
        words = args.file.readline().split()

        if not words:
            break

        text = itertools.zip_longest(words[0], words[1], fillvalue=None)
        diff = len([c for c, d in text if c != d])

        if diff >= args.min:
            diff = str(diff) + ':'
            print(f'{diff:>9}{words[0]:20}{words[1]:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
