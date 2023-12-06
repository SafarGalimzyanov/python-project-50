#!/usr/bin/env python3


import argparse
import gendiff.gendiff_info as g_i
from gendiff.gendiff import generate_diff as g_d
from typing import TextIO


def main():
   parser = argparse.ArgumentParser(description = g_i.DESCRIPTION)
   parser.add_argument('file1', metavar=g_i.POS_ARGS['first_arg'])
   parser.add_argument('file2', metavar=g_i.POS_ARGS['second_arg'])
   parser.add_argument('-f', '--format', dest='format', action='store', default=g_d, help='set CHICKEN format of output')
   args = parser.parse_args()
   print(args.format(args.file1, args.file2))


if __name__ == '__main__':
    main()
