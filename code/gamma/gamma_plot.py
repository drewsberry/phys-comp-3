from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex=True)

def plot_times_and_distances(lifetimes, decay_positions):
    # Plot decay times and distances

    num_bins = 50

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

    plt.savefig("plots/gamma_decays.eps", bbox_inches="tight")

    return True

def plot_decay_angles(phi, theta):
    # Plot histogram of decay angles

    num_bins = 200

    fig = plt.figure()

    plt.hist2d(phi, theta, bins=num_bins)
    plt.xlabel("Azimuth, $\\theta$")
    plt.ylabel("Altitude, $\\varphi$")
    plt.title("Random Decay Angles")

    cbar = plt.colorbar()
    cbar.solids.set_edgecolor("face")
    plt.draw()

    plt.savefig("plots/gamma_angles.eps", bbox_inches="tight")

    return True

def plot_detector(x_pos, y_pos, detector_range):
    # Plot detector readings

    x_res = 0.1 # cm
    y_res = 0.3 # cm

    num_bins = (((detector_range[0][1] - detector_range[0][0]) / 0.1),
                ((detector_range[1][1] - detector_range[1][0]) / 0.3))

    fig = plt.figure()

    plt.hist2d(x_pos, y_pos, bins=num_bins, range=detector_range)
    plt.xlabel("$x$ position on detector, m")
    plt.ylabel("$y$ position on detector, m")
    plt.title("$\gamma$ Ray Detector Readings")

    plt.savefig("plots/gamma_detector.eps", bbox_inches="tight")

    return True
