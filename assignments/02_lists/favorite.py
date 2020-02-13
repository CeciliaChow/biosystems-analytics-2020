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
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description=' My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Some things')

    parser.add_argument('-s',
                        '--sep',
                        metavar='str',
                        type=str,
                        default=', ',
                        help='A separator')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if num == 1:
        print(f'{items[0]}\n'
              f'This is one of my favorite things.')

    else:
        things = args.sep.join(items)
        print('{}\nThese are a few of my favorite things.'.format(things))


# --------------------------------------------------
if __name__ == '__main__':
    main()
