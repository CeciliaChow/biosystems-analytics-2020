#!/usr/bin/env python3
"""Dear Ken, after today class, I am more comfortable with coding this program.
Although I have a trouble passing the test, I feel like I have learnt a lot
from coding this. I was hoping to get some credits form handing in still
as I have been working really hard for this."""

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
        description='Filter SwissPort file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Swiss file')

    parser.add_argument('-k',
                        '--keyword',
                        metavar='keyword',
                        type=str,
                        required=True,
                        nargs='+',
                        help='Keyword to take')

    parser.add_argument('-s',
                        '--skiptaxa',
                        metavar='[taxa [taxa ...]]',
                        type=str,
                        nargs='*',
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
    keyword = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))
    num_skipped = 0
    num_taken = 0

    out_fh = open(args.outfile, "wt")

    for rec in SeqIO.parse(args.FILE, 'swiss'):
        annot = rec.annotations

        if skip_taxa and 'taxonomy' in annot:
            taxa = set(map(str.lower, annot['taxonomy']))
            if skip_taxa.intersection(taxa):
                num_skipped += 1
                continue

        keywords = annot.get('keywords')

        if keywords:
            keywords = set(map(str.lower, keywords))
            if keyword.intersection(keywords):
                num_taken += 1
                SeqIO.write(rec, out_fh, 'fasta')
            else:
                num_skipped += 1

    out_fh.close()

    print(f'Done, skipped {num_skipped} and took {num_taken}.'
          f' See output in "{args.outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
