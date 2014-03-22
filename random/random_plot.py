import math
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc("text", usetex=True)

def plot_sin_hist(dist, title=None, fname=None):
    # Plot dist as histogram, with sin curve plotted over the top

    num_bins = 100
    bin_width = math.pi / num_bins
    num = len(dist)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(dist, num_bins, color="green", linewidth=0.5, label="Sinusoidal random number")

    x = np.arange(0, math.pi, 0.01)
    plt.plot(x, (num/2)*bin_width*np.sin(x), linewidth=5, label="$\\sin(\\theta)$")

    plt.xlim([0,math.pi])

    plt.xlabel("Random angle, $\\theta$")
    plt.ylabel("Frequency")
    plt.title(title)

    plt.legend(loc="upper right", fontsize="x-small", borderpad=1)

    if fname == None:
        now = datetime.now()
        fname = "plots/"+"random_sinusoid_"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)+".eps"
    else:
        fname = "plots/"+fname+".eps"

    plt.savefig(fname)
    print "Saved plot as {}".format(fname)

def plot_gen_hist(dist, title=None, fnam=None, func_str=None, plot_range=(0,1)):
    # Plot dist as histogram, with func curve plotted over top

    num_bins = 100
    bin_width = math.pi / num_bins
    num = len(dist)

    if func_str:
        func = rndlib.string_to_func(func_str)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(dist, num_bins, color="green", linewidth=0.5, label="Random number distribution")

    if func_str:
        x = np.arange(plot_range[0], plot_range[1], 0.01)
        plt.plot(x, (num/2)*bin_width*func(x), linewidth=5, label=func)

    # plt.xlim([plot_range[0],plot_range[1]])
    plt.xlim(plot_range)

    plt.xlabel("Random number, $x$")
    plt.ylabel("Frequency")
    plt.title(title)

    plt.legend(loc="upper right", fontsize="x-small", borderpad=1)

    if fname == None:
        now = datetime.now()
        fname = "plots/"+"random_sinusoid_"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)+".eps"
    else:
        fname = "plots/"+fname+".eps"

    plt.savefig(fname)
    print "Saved plot as {}".format(fname)
