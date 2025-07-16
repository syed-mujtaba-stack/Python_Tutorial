# Day 27 Solution: Advanced CLI & argparse
import argparse

parser = argparse.ArgumentParser(description='Count lines in a file')
parser.add_argument('filename', type=str, help='File to read')
parser.add_argument('--verbose', action='store_true', help='Print each line')
args = parser.parse_args()

with open(args.filename) as f:
    lines = f.readlines()
    print('Line count:', len(lines))
    if args.verbose:
        for line in lines:
            print(line, end='')
