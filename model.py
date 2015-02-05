#!/usr/bin/env python
# vim: set fileencoding=utf-8 shiftwidth=4 tabstop=4 expandtab smartindent :
"""
A simple single-layer climate model.
"""

import argparse

def Tj(fs = 1370, a = 0.28, sigma = 5.67E-8, f = 0.77):
	return (fs*(1-a)/(4*sigma*(1-(f/2))))**(1/4)

def main():
	"""
    Main function for running the model.
    Options will be parsed from the command line.
    """
	print("%d" % (Tj()))

def parse_args():
    parser = argparse.ArgumentParser(description='A single-layer climate model.')
    parser.add_argument('-fs', type=float, default=1370, help='Sun constant')
    parser.add_argument('-a', type=float, default=0.28, help='Albedo')
    parser.add_argument('-sigma', type=float, default=6.67E-8, help='Stefan-Boltzmanns constant')
    parser.add_argument('-f', type=float, default=0.77, help='Absorption capacity of the atmosphere')

    return parser.parse_args()

if __name__ == "__main__":
    main()
