# In-built libraries
from datetime import datetime

# External libraries
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np

# Custom libraries
import analytic_sin_io as anaio

rc("text", usetex=True)

def plot_hist(dist, title="Analytically Produced Random Sin Distribution", fname="analyltic_sin"):
    # Plot dist as histogram, with sin curve plotted over the top

    if not anaio.is_valid_fname(fname):
        print "[Error] Invalid filename:", fname
        print "[Error] Please use only lower and upper alphanumerics, full stop, underscore and hyphen."
        print "[Error] Data not plotted to eps file."
        return False

    num_bins = 100
    bin_width = np.pi / num_bins
    num = len(dist)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(dist, num_bins, color="green", linewidth=0.5, label="Sinusoidal random number")

    x = np.arange(0, np.pi, 0.01)
    plt.plot(x, (num/2)*bin_width*np.sin(x), linewidth=5, label="$\\sin(\\theta)$")

    plt.xlim([0,np.pi])

    plt.xlabel("Random angle, $\\theta$")
    plt.ylabel("Frequency")
    plt.title(title)

    plt.legend(loc="upper right", fontsize="x-small", borderpad=1)

    fname = "plots/" + fname + ".eps"

    plt.savefig(fname)
    print "Plot saved as {}".format(fname)
