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
        description='Filter SwissProt file for keywords, taxa',
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
    keyword = args.keyword.lower()
    skip_taxa = set(map(str.lower, args.skiptaxa or []))
    num_skipped = 0
    num_taken = 0

    for rec in SeqI0.parse(args.file, 'swiss'):
        annot = rec.annotations

        if skip_taxa and 'taxonomy' in annot:
            taxa = set(map(str.lower, taxa), annot['taxonomy'])
            if skip_taxa.intersection(taxa):
                num_skipped += 1
            continue

        if 'keywords' in annot:
            kw = set(map(str.lower, annot['keywords']))

        if keyword in kw:
            num_taken += 1
            SeqIO.write(rec, args.outfile, 'fasta')
        else:
            num_skipped += 1

        break

    print(f'Done, skipped {num_skipped} and took {num_taken}.'
          f'Sees output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
