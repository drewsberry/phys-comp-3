from __future__ import division

# External plotting libraries
import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex=True)

def plot_times_and_distances(lifetimes, decay_positions, num_bins=50,
                             fname="gamma_decays"):
    # Plot decay times and distances

    fig = plt.figure()

    plt.subplot(2,1,1)
    plt.hist(lifetimes, num_bins, color="red")
    plt.xlabel("Time, s$^{-1}$")
    plt.ylabel("Relative Frequency")
    plt.title("Random Decay Times")

    plt.subplot(2,1,2)
    plt.hist(decay_positions, num_bins, color="blue")
    plt.xlabel("Position from injection point, m$^{-1}$")
    plt.ylabel("Relative Frequency")
    plt.title("Random Decay Position")

    plt.tight_layout()

    fname = "plots/" + fname + ".eps"
    plt.savefig(fname, bbox_inches="tight")
    print "Plot saved as {}".format(fname)

    return True

def plot_decay_angles(phi, theta, num_bins=200, fname="gamma_angles"):
    # Plot histogram of decay angles

    fig = plt.figure()

    plt.hist2d(phi, theta, bins=num_bins)
    plt.xlabel("Azimuth, $\\theta$")
    plt.ylabel("Altitude, $\\varphi$")
    plt.title("Random Decay Angles")

    cbar = plt.colorbar()
    cbar.solids.set_edgecolor("face")
    plt.draw()

    fname = "plots/" + fname + ".eps"
    plt.savefig(fname, bbox_inches="tight")
    print "Plot saved as {}".format(fname)

    return True

def plot_detector(x_pos, y_pos, detector_range, res_x, res_y, 
                  title="$\gamma$ Ray Detector Readings", fname="gamma_detector"):
    # Plot detector readings

    num_bins = (((detector_range[0][1] - detector_range[0][0]) / res_x),
                ((detector_range[1][1] - detector_range[1][0]) / res_y))

    fig = plt.figure()

    plt.hist2d(x_pos, y_pos, bins=num_bins, range=detector_range)
    plt.xlabel("$x$ position on detector, m")
    plt.ylabel("$y$ position on detector, m")
    plt.title(title)

    cbar = plt.colorbar()
    cbar.solids.set_edgecolor("face")
    plt.draw()

    fname = "plots/" + fname + ".eps"
    plt.savefig(fname, bbox_inches="tight")
    print "Plot saved as {}".format(fname)

    return True
