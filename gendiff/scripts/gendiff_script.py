#!/usr/bin/env python3


import argparse
import gendiff.gendiff_info as gendiff_info
from gendiff.gendiff_engine import generate_diff
from gendiff.gendiff_parse import generate_parse


def main():
   parser = argparse.ArgumentParser(description = gendiff_info.DESCRIPTION)
   parser.add_argument('file1')
   parser.add_argument('file2')
   parser.add_argument('-f', '--format', dest='format', action='store', default='', help='set format of output')
   args = parser.parse_args()
   parsed = generate_parse(args.file1, args.file2, args.format)
   result = generate_diff(*parsed)
   print(result)


if __name__ == '__main__':
    main()
