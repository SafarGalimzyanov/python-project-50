#!/usr/bin/env python3


import argparse
import gendiff.gendiff_info as gendiff_info
from gendiff.gendiff_engine import generate_output
from gendiff.gendiff_parse import generate_parse


def main():
   parser = argparse.ArgumentParser(description = gendiff_info.DESCRIPTION)
   parser.add_argument('file1', metavar=gendiff_info.POS_ARGS['first_arg']) #?
   parser.add_argument('file2', metavar=gendiff_info.POS_ARGS['second_arg']) #?
   parser.add_argument('-f', '--format', dest='format', action='store', default=generate_parse, help='set CHICKEN format of output')
   args = parser.parse_args()
   print(generate_output(*args.format(args.file1, args.file2, args.format)))


if __name__ == '__main__':
    main()
