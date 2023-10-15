#!/usr/bin/env python3


import argparse
import gendiff.gendiff_info as g_i
from gendiff.gendiff import generate_diff
from typing import TextIO


def main():
   parser = argparse.ArgumentParser(description = g_i.DESCRIPTION)
   parser.add_argument('text_file1', metavar=g_i.POS_ARGS['first_arg'])
   parser.add_argument('text_file2', metavar=g_i.POS_ARGS['second_arg'])

   parser.add_argument('-f', '--format', dest='FORMAT', default=generate_diff, help='set format of output')
   args = parser.parse_args()
   print(args.default(args.text_file1, args.text_file2))
   #print(args.text_file)


if __name__ == '__main__':
    main()
