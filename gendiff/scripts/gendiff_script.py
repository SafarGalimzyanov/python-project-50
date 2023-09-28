#!/usr/bin/env python3


import argparse
import gendiff.gendiff_info as g_i
from typing import TextIO


def main():
   parser = argparse.ArgumentParser(description = g_i.DESCRIPTION)
   parser.add_argument('text_file', metavar=g_i.POS_ARGS['first_arg'], type=TextIO)
   parser.add_argument('text_file', metavar=g_i.POS_ARGS['second_arg'], type=TextIO)

   parser.add_argument('-f', '--format', dest='FORMAT', help='set format of output')
   args = parser.parse_args()
   print(args.dest(args.text_file))


if __name__ == '__main__':
    main()
