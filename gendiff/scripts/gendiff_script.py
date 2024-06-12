#!/usr/bin/env python3


import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('file1')
    parser.add_argument('file2')
    parser.add_argument('-f', '--format', dest='format', action='store', help='set format of output')
    args = parser.parse_args()
    result = generate_diff(args.file1, args.file2, args.format)
    
    print(result)


if __name__ == '__main__':
    main()
