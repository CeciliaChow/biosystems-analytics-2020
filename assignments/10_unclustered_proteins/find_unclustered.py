#!/usr/bin/env python3
"""HW"""

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
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--cdhit',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        required=True,
                        help='Output file from CD-HIT (clustered proteins)')

    parser.add_argument('-p',
                        '--proteins',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required=True,
                        help='Proteins FASTA')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='outfile',
                        type=str,
                        default='unclustered.fa',
                        help='Output file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    protein_ids = set()

    for line in args.cdhit:

        match = re.search(r'>(\d+)', line)

        if match:
            protein_ids.add(match.group(1))

    count_unc = 0

    count_tot = 0

    out_fh = open(args.outfile, "wt")

    for rec in SeqIO.parse(args.proteins, 'fasta'):

        prot_id = re.sub(r'\|.*', '', rec.id)
        count_tot += 1

        if prot_id not in protein_ids:
            SeqIO.write(rec, out_fh, 'fasta')
            count_unc += 1

    out_fh.close()

    print(f'Wrote {count_unc:,} of {count_tot:,} unclustered proteins to "{args.outfile}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
