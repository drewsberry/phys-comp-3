from __future__ import division

import numpy as np

import sphere_mayavi_lib as sphmaylib

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

print "Producing random decay times..."
num_events_per_sec = np.random.poisson(frequency, num_decays)

lifetimes = 1 / num_events_per_sec
print "...done\n"

print "Calculating random decay positions..."
decay_positions = lifetimes*speed

dists_from_detector = inj_to_det_dist - decay_positions
print "...done\n"

print "Producing random angles..."
azimuths = np.arccos(2*np.random.random(num_decays) - 1)
altitudes = 2*np.pi*np.random.random(num_decays)

even_azimuths = np.random.uniform(0, np.pi, num_decays)
even_altitudes = np.random.uniform(0, 2*np.pi, num_decays)
print "...done\n"
print "...done\n"

print "Trying out crazy mayavi thing...\n"
sphmaylib.plot_spheres(azimuths, altitudes, even_azimuths, even_altitudes)
print "\nSuccess!"
