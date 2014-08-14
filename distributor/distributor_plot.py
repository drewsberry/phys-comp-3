from __future__ import division

# External libraries
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np

# Custom libraries
import str_to_func_lib as stfl
import distributor_io as dstio

rc("text", usetex=True)

def plot_hist(dist, func_str, plot_range, title="Randomly Distributed Numbers", fname="distribution"):
    # Plot dist as histogram, with func curve plotted over top

    if not dstio.is_valid_fname(fname):
        print "[Error] Invalid filename:", fname
        print "[Error] Please use only lower and upper alphanumerics, full stop, underscore and hyphen."
        print "[Error] Data not plotted to eps file."
        return False

    num_bins = 100
    dx = 0.00001 # Precision to which function line is plotted
    bin_width = (plot_range[1] - plot_range[0]) / num_bins
    num = len(dist)

    func = stfl.string_to_function(func_str)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(dist, num_bins, color="green", linewidth=0.5, 
                               label="Random {} distribution".format(func_str))

    x = np.arange(plot_range[0], plot_range[1], dx)

    # Use composite trapezoidal rule to integrate function within range
    func_area = np.trapz(func(x), dx=dx)

    # Normalisation factor so curve and histogram are level
    norm = num*bin_width/func_area

    plt.plot(x, norm*func(x), linewidth=5, label=func_str)

    plt.xlim(plot_range)

    plt.xlabel("Random number, $x$")
    plt.ylabel("Frequency")
    plt.title(title)

    plt.legend(loc="upper right", fontsize="x-small", borderpad=1)

    fname = "plots/" + fname + ".eps"

    plt.savefig(fname)
    print "Plot saved as {}".format(fname)
