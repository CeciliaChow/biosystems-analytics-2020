#!/usr/bin/env python3
"""
Author : ceciliachow
Date   : 2020-02-06
Purpose: Rock the Casbah
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='str',
                        help='A vowel to look for',
                        type=str,
                        choices=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='The text to search')

    return parser.parse_args()

    # --------------------------------------------------


def main():
    """main"""
    args = get_args()
    count = len(args.text)

    for x in range(len(args.text)):
        if args.text[x] == args.vowel:
            print(f'Found "{args.vowel}" in "{args.text}" at index {x}.')
            count = count - 1
        else:
            continue

    if count == len(args.text):
        print(f'"{args.vowel}" is not found in "{args.text}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
