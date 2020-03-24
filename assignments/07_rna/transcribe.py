#!/usr/bin/env python3
"""
Author : CeciliaChow
Date   : 2020-03-23
Purpose: transcribe.py
"""

import argparse
import sys
import io
import os


# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file(s)',
                        nargs='+')

    parser.add_argument('-o',
                        '--outdir',
                        metavar='DIR',
                        type=str,
                        default="out",
                        help='Output directory')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    count_seq = 0

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    for fh in args.FILE:
        out_file = os.path.join(args.outdir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        while True:
            seq = fh.readline().split()

            if not seq:
                break

            count_seq += 1

            out_fh.write(seq[0].replace('T', 'U').rstrip()+'\n')

        out_fh.close()
        
    if count_seq < 2:
        seq_str = 'sequence'
    else:
        seq_str = 'sequences'

    if len(args.FILE) < 2:
        file_str = 'file'
    else:
        file_str = 'files'

    print(f'Done, wrote {count_seq} {seq_str} in {len(args.FILE)} {file_str } to directory "{args.outdir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
