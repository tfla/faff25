#!/usr/bin/env python
# vim: set fileencoding=utf-8 shiftwidth=4 tabstop=4 expandtab smartindent :
"""
A simple single-layer climate model.
"""

__author__ = "Timmy Larsson, Linus Lexfors, Hans Bjerndell"
__license__ = "GPLv2"

import argparse, numpy
import matplotlib.pyplot as plt

def Tj():
    return (args.fs*(1-args.a)/(4*args.sigma*(1-(args.f/2))))**(1/4)

def main():
    """
    Main function for running the model.
    Options will be parsed from the command line.
    """
    global args 
    args = parse_args()
    #print("Average temp for earth is %d K" % (Tj()))
    plotrange2()

def plotrange():
    results=[]
    x = numpy.arange(0, 1.01, 0.01)
    for i in x:
        args.a = i
        temp = Tj()
        print("Temp with a = ", i, " is ", temp)
        results.append(temp)
    plt.ylabel('Tj (K)')
    plt.xlabel('Albedo')
    plt.plot(x, results)
    plt.show()

def plotrange2():
    results=[]
    x = numpy.arange(0, 2.0, 0.01)
    for i in x:
        args.f = i
        temp = Tj()
        print("Temp with f = ", i, " is ", temp)
        results.append(temp)
    plt.ylabel('Tj (K)')
    plt.xlabel('f')
    plt.plot(x, results)
    plt.show()

def parse_args():
    parser = argparse.ArgumentParser(description='A single-layer climate model.')
    parser.add_argument('-fs', type=float, nargs='?', default=1370, help='Sun constant')
    parser.add_argument('-a', type=float, nargs='?', default=0.28, help='Albedo')
    parser.add_argument('-sigma', type=float, nargs='?', default=5.67E-8, help='Stefan-Boltzmanns constant')
    parser.add_argument('-f', type=float, nargs='?', default=0.77, help='Absorption capacity of the atmosphere')

    return parser.parse_args()

if __name__ == "__main__":
    main()
