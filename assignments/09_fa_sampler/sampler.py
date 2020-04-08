#!/usr/bin/env python3
"""HW"""

import argparse
import os
import sys
import Bio
import random
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input FASTA file(s)',
                        nargs='+')

    parser.add_argument('-p',
                        '--pct',
                        metavar='reads',
                        type=float,
                        default=0.1,
                        help='Percent of reads')

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        type=int,
                        help='Random seed value')

    parser.add_argument('-o',
                        '--outdir',
                        metavar='DIR',
                        type=str,
                        default='out',
                        help='Output directory')

    args = parser.parse_args()

    if not 0 < args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    random.seed(args.seed)

    count_file, count_seq = 1, 0

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    for fh in args.FILE:

        basename = os.path.basename(fh.name)

        out_file = os.path.join(args.outdir, basename)

        print(f'  {count_file}: {basename}')

        count_file += 1

        out_fh = open(out_file, "wt")

        for rec in SeqIO.parse(fh, 'fasta'):

            if random.random() < args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                count_seq += 1

        out_fh.close()

    file_str = 'file' if len(args.FILE) <= 1 else 'files'

    print(f'Wrote {count_seq:,} sequences from {len(args.FILE)} {file_str} to directory "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
