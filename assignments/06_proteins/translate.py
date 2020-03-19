#!/usr/bin/env python3
"""
Author : CeciliaChow
Date   : 2020-02-29
Purpose: hamming.py
"""

import argparse
import sys
import io


# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        type=str,
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='A file with codon translations',
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=str,
                        default="out.txt",
                        help='Output filename')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out_fh = open(args.outfile, "wt")

    lookup = {line[0:3].upper(): line[3:].strip() for line in args.codons}

    seq = args.str.upper()

    k = 3

    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
        if codon in lookup:
            if lookup[codon] == 'Stop':
                break
            else:
                out_fh.write(lookup[codon])
        else:
            out_fh.write('-')

    out_fh.close()

    print(f'Output written to "{args.outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
