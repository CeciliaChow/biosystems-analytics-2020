#!/usr/bin/env python3
"""Hello Ken, I have tried really hard to understand what the assignment is asking us to do. However, after a long
digestion I still find it confusing. The main difficulty for me is I am confused what the assignment wants us to write
 in the output. I completed all get_args part but even spending more than the request time (I have spent more than 6 hrs
 to read other related information still I am not following what the task of this program is. I feel really bad as this
  breaks my track record handing in all assignments and got the program passed all tests before class every time but not
 this time."""


import argparse
import os
import sys
import Bio
import random
from Bio import SeqIO
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        metavar='keyword',
                        type=str,
                        required=True,
                        help='Keyword to take')

    parser.add_argument('-s',
                        '--skiptaxa',
                        metavar='[taxa [taxa ...]]',
                        type=str,
                        help='Taxa to skip')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=str,
                        default='out.fa',
                        help='Output filename')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print('hi')


# --------------------------------------------------
if __name__ == '__main__':
    main()
