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

num_decays = 100000

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

even_azimuths = np.random.uniform(0, math.pi, num_decays)
even_altitudes = np.random.uniform(0, 2*math.pi, num_decays)
print "...done\n"
print "...done\n"

# scat_paths = plt.scatter(azimuths, altitudes)
# scat_points = scat.get_paths()

scat_points = [azimuths, altitudes]

print "Trying out crazy mayavi thing...\n"

# Create a sphere
r = 0.3
pi = np.pi
cos = np.cos
sin = np.sin
theta, phi = np.mgrid[0:pi:200j, 0:2*pi:200j]

print "Converting phi and theta into x,y and z"
x = r * sin(theta) * cos(phi)
y = r * sin(theta) * sin(phi)
z = r * cos(theta)
print "...done\n"

print "Converting data points from spherical to Cartesian coords..."
x_points = r * sin(azimuths) * cos(altitudes)
y_points = r * sin(azimuths) * sin(altitudes)
z_points = r * cos(azimuths)

x_points_even = r * sin(even_azimuths) * cos(even_altitudes)
y_points_even = r * sin(even_azimuths) * sin(even_altitudes)
z_points_even = r * cos(even_azimuths)
print "...done"

mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
mlab.clf()

print "Making spherical surface plot..."
mlab.mesh(x, y, z, color=(1,0,0))
mlab.points3d(x_points_even, y_points_even, z_points_even, mode="point")
mlab.text3d(0, 0, 0.5, "Incorrect", scale=0.1)

mlab.mesh(x+0.5, y+0.5, z+0.5, color=(0,0,1))
mlab.points3d(x_points+0.5, y_points+0.5, z_points+0.5, mode="point")
mlab.text3d(0.5, 0.5, 1.0, "Correct", scale=0.1)

mlab.title("Point Picking on a Sphere")
print "...done\n"

print "Showing result..."
mlab.show()
print "...done"

print "\nSuccess!"
