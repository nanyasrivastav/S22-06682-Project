#!/usr/bin/env python 

from read_data import display_head

def main(args):
    for fname in args.infile:
        display_head(fname, args.num)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Display Dataset')
    parser.add_argument('-n', '--num', type=int, help='# rows to display')
    parser.add_argument('infile', type=str, nargs='*', default='-', help='Input file name(s)')
    args = parser.parse_args()
    main(args)

