#!/usr/bin/env python3
"""
Author : CeciliaChow
Date   : 2020-02-25
Purpose: head.py
"""

import argparse
import sys
import os


# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        metavar='int',
                        type=int,
                        default=10,
                        help='Number of lines')

    args = parser.parse_args()

    if not 1 <= args.num:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in range(args.num):
        print(args.file.readline().rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
