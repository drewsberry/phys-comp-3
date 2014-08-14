from __future__ import division

import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

from mayavi import mlab

rc("text", usetex=True)

# Given constants
speed = 2000 # m/s
mean_lifetime = 520e-6 # microseconds
micro = 1e-6 # For microsecond to second conversions
res_x = 10 # cm
res_y = 30 # cm
inj_to_det_dist = 2.0 # m; injector to detector distance

# Calculated constants
frequency = 1 / mean_lifetime

num_decays = int(1e7)

# Lifetimes follow Poisson distribution with mean 520 microseconds
# lifetimes = np.random.poisson(mean_lifetime, num_decays)

print "Producing random decay times..."
num_events_per_sec = np.random.poisson(frequency, num_decays)

lifetimes = 1 / num_events_per_sec
print "...done\n"

# Position is time * velocity

print "Calculating random decay positions..."
decay_positions = lifetimes*speed

dists_from_detector = inj_to_det_dist - decay_positions
print "...done\n"

# Next I need to pick two random rangles, the azimuth, phi, and the polar angle or altitude, theta.
# I need to be careful about how I choose my random angle... I shouldn't choose it to be even in the lab frame.

print "Producing random angles..."
azimuths = np.arccos(2*np.random.random(num_decays) - 1)
altitudes = 2*math.pi*np.random.random(num_decays)
print "...done\n"

print "Calculating detector positions..."
x_pos = dists_from_detector*np.tan(azimuths)
y_pos = dists_from_detector*np.tan(altitudes)
print "...done\n"

num_bins = 50

print "Plotting decay times and positions to eps file..."
fig1 = plt.figure()

decay_time_ax = plt.subplot(2,1,1)
decay_time_ax.hist(lifetimes, num_bins, color="red")
decay_time_ax.set_xlabel("Time /s")
decay_time_ax.set_ylabel("Frequency")
decay_time_ax.set_title("Random Decay Times")

decay_pos_ax = plt.subplot(2,1,2)
decay_pos_ax.hist(decay_positions, num_bins, color="blue")
decay_pos_ax.set_xlabel("Position from injection point /m")
decay_pos_ax.set_ylabel("Frequency")
decay_pos_ax.set_title("Random Decay Position")

plt.tight_layout()

plt.savefig("plots/gamma_decays.eps", bbox_inches="tight")
print "...done\n"

num_bins = 200
detector_range = ((-5,5),(-5,5))

print "Plotting decay angles and detector readings to eps file..."
fig2 = plt.figure()

decay_angles_ax = plt.subplot(2,1,1)
ang_counts, ang_xedges, ang_yedges, ang_Image = decay_angles_ax.hist2d(azimuths, altitudes, bins=num_bins)
decay_angles_ax.set_xlabel("Azimuth, $\\varphi$")
decay_angles_ax.set_ylabel("Altitude, $\\theta$")
decay_angles_ax.set_title("Random Decay Angles")

detector_pos_ax = plt.subplot(2,1,2)
detector_pos_ax.hist2d(x_pos, y_pos, bins=num_bins, range=detector_range)
detector_pos_ax.set_xlabel("$x$ position on detector")
detector_pos_ax.set_ylabel("$y$ position on detector")
detector_pos_ax.set_title("$\gamma$ Ray Detector Readings")

plt.tight_layout()

plt.savefig("plots/gamma_hists.eps", bbox_inches="tight")

print "...done\n"

# scat_paths = plt.scatter(azimuths, altitudes)
# scat_points = scat.get_paths()

print "Trying out crazy mayavi thing...\n"

# Create a sphere
r = 0.3
pi = np.pi
cos = np.cos
sin = np.sin
theta, phi = np.mgrid[0:pi:200j, 0:2*pi:200j]

# ang_xedges = np.delete(ang_xedges, -1)
# ang_yedges = np.delete(ang_yedges, -1)

# print "Converting azimuths and altitudes into 2d arrays..."
# phi = np.array([[j for i in range(len(ang_xedges))] for j in ang_xedges])
# theta = np.array([[j for i in range(len(ang_yedges))] for j in ang_yedges])
# print "...done\n"

print "Converting phi and theta into x,y and z"
x = r * sin(theta) * cos(phi)
y = r * sin(theta) * sin(phi)
z = r * cos(theta)
print "...done\n"

mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
mlab.clf()

print "Making spherical surface plot..."
# mlab.mesh(x, y, z, scalars=ang_counts, colormap='jet')
mlab.mesh(x, y, z, scalars=ang_counts, colormap='jet')
print "...done\n"

print "Showing result..."
mlab.show()
print "...done"

print "\nSuccess!"
