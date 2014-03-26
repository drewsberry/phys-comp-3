from __future__ import division

import math

# In-built libraries
from datetime import datetime

# External libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Custom libraries
import str_to_func_lib as stfl

matplotlib.rc("text", usetex=True)

def plot_gen_hist(dist, func_str, title=None, fname=None, plot_range=(0,1)):
    # Plot dist as histogram, with func curve plotted over top

    num_bins = 100
    dx = 0.0001
    bin_width = (plot_range[1] - plot_range[0]) / num_bins
    num = len(dist)

    func = stfl.string_to_function(func_str)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(dist, num_bins, color="green", linewidth=0.5, 
                               label="Random {} distribution".format(func_str))

    x = np.arange(plot_range[0], plot_range[1], dx)

    func_area = np.trapz(func(x), dx=dx)
    # Use composite trapezoidal rule to integrate function within range

    norm = num*bin_width/func_area
    # Normalisation factor so curve and histogram are level

    plt.plot(x, norm*func(x), linewidth=5, label=func_str)

    plt.xlim(plot_range)

    plt.xlabel("Random number, $x$")
    plt.ylabel("Frequency")
    plt.title(title)

    plt.legend(loc="upper right", fontsize="x-small", borderpad=1)

    if fname:
        fname = "plots/"+fname+".eps"
    else:
        now = datetime.now()
        fname = "plots/"+"random_sinusoid_"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)+".eps"

    plt.savefig(fname)
    print "Saved plot as {}".format(fname)
