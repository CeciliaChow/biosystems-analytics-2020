#!/usr/bin/env python3
"""
Author : CeciliaChow
Date   : 2020-02-18
Purpose: days.py
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description=' What to do on each day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Days of the week')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    jumper = {'Monday': 'On Mondays I never go to work', 'Tuesday': 'On Tuesdays I stay at home',
              'Wednesday': 'On Wednesdays I never feel inclined', 'Thursday': 'On Thursdays, it\'s a holiday',
              'Friday': 'And Fridays I detest', 'Saturday': 'Oh, it\'s much too late on a Saturday',
              'Sunday': 'And Sunday is the day of rest'}
    for x in args.item:
        if x in jumper.keys():
            print(jumper.get(x, x), end='\n')
        else:
            print(f'Can\'t find "{x}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
