#!/usr/bin/env python
# vim: set fileencoding=utf-8 shiftwidth=4 tabstop=4 expandtab smartindent :
"""
A simple single-layer climate model.
"""

__author__ = "Timmy Larsson, Linus Lexfors, Hans Bjerndell"
__license__ = "GPLv2"

import argparse, numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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
    plotrange()
    plotrange2()

def plotrange():
    results=[]
    x = numpy.arange(0, 1.01, 0.01)
    for i in x:
        args.a = i
        temp = Tj()
        print("Temp with a = ", i, " is ", temp)
        results.append(temp)
    plt.ylabel('Tj (K)', fontsize=18)
    plt.xlabel('Albedo', fontsize=18)
    plt.plot(x, results)
    plt.show()

def plotrange2():
    results=[]
    x = numpy.arange(0, 1.01, 0.01)
    for i in x:
        args.f = i
        temp = Tj()
        print("Temp with f = ", i, " is ", temp)
        results.append(temp)
    plt.ylabel('Tj (K)', fontsize=18)
    plt.xlabel('f', fontsize=18)
    plt.plot(x, results)
    plt.show()

def plotrange3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    results=[]
    X=[]
    Y=[]
    x = numpy.arange(0, 1.01, 0.01)
    for i in x:
        args.a = i
        y = numpy.arange(0, 1.01, 0.01)
        for j in y:
            args.f = j
            temp = Tj()
            print("Temp with f = ", j, " and a = ", i, " is ", temp)
            results.append(temp)
            X.append(i)
            Y.append(j);
    
    print(len(X))
    print(len(Y))
    print(len(results))
    surf = ax.plot_surface(X, Y, results, rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

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
