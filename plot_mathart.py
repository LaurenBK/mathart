# Adapted from https://github.com/marcusvolz/mathart/blob/master/R/bird_in_flight.R

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import sys
sys.path.append('python_functions/')
import argparse
import seaborn as sns 


def plot_lines(data, name):
    lc = mc.LineCollection(data, linewidths=0.02)
    fig = plt.figure(3,3)
    ax = plt.subplots(1,1,1)
    ax.add_collection(lc)
    ax.autoscale()
    plt.savefig(f'python_plots/{name}')


def plot_circles(data, name):
    fig = plt.figure(3,3)
    ax = plt.subplots(1,1,1)
    plt.scatter(data[:, 0], data[:, 1], s=1000*data[:, 2], facecolor="none", edgecolor='k', alpha=0.1)
    plt.savefig(f'python_plots/{name}')


def plot_variable_alpha(data, name):
    alphas = data[:, 2]
    rgba_colors = np.zeros((len(alphas), 4))
    rgba_colors[:, 3] = alphas 
    print(np.min(alphas), np.max(alphas))
    plt.scatter(data[:, 0], data[:, 1], s=2, color=rgba_colors)
    plt.savefig(f'python_plots/{name}')


def plot_normal(data, name):
    plt.plot(data[:, 0], data[:, 1], alpha=0.7)
    plt.savefig(f'python_plots/{name}')


def plot(name, circles=True):
    module = __import__(name)
    func = getattr(module, name)
    data = func()

    if data.shape[1] == 4:
        plot_lines(data, name)
    elif data.shape[1] == 3:
        if circles:
            plot_circles(data, name)
        else:
            plot_variable_alpha(data, name)
    elif data.shape[1] == 2:
        plot_normal(data, name)
    else:
        print(data.shape)
        raise KeyError('The returned data is not in a plottable form')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='Name of file to convert to python')
    circle_parser = parser.add_mutually_exclusive_group(required=False)
    circle_parser.add_argument('--circles', dest='circles', 
        help='Plot circles with r-value', action='store_true')
    circle_parser.add_argument('--no-circles', dest='circles',
        help='Plot variable-alpha with r-value', action='store_false')
    parser.set_defaults(circles=True)
    args = parser.parse_args()

    name = args.filename 
    plot(name, circles)
