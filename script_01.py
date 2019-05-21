#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='An example python script, ready for extensions.')
parser.add_argument('--jens', action = 'store_true')
parser.add_argument('--carsten', action = 'store_true')

args = parser.parse_args()

print("Hello, Loosolab!")

if(args.jens):
    print("Hello, Jens!")
if(args.carsten):
    print("Hello, Superman!")
