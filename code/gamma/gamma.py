from __future__ import division

import math
import argparse

import numpy as np

import gamma_lib as gamlib
import gamma_plot as gamplt

parser = argparse.ArgumentParser(description="Simulating the decay of injected nuclei travelling towards a detector.")

parser.add_argument("-r", "--range", default="((-2.5,2.5),(-2.5,2.5))",
                    help="range of detector. Enter as python tuple in string form without spaces, e.g. '((-5,5),(-5,5))'")

parser.add_argument("-n", "--num", type=float, default=1e7,
                    help="The number of decays to simulate.")

parser.add_argument("-s", "--speed", type=float, default=2000,
                    help="Speed of injected unstable nuclei, in meters per second.")

parser.add_argument("-l", "--lifetime", type=float, default=520,
                    help="Average lifetime of unstable nucleus, in microseconds.")

parser.add_argument("-xr", "--xres", type=float, default=10,
                    help="x resolution of detector in centimetres,")

parser.add_argument("-yr", "--yres", type=float, default=30,
                    help="y resolution of detector in centimetres,")

parser.add_argument("-d", "--distance", type=float, default=2,
                    help="distance from injection point to detector, in meters.")

args = parser.parse_args()

num_decays = int(args.num)
mean_lifetime = args.lifetime*1e-6 # microseconds
res_x = args.xres / 100 # cm -> m
res_y = args.yres / 100 # cm -> m
inj_to_det_dist = args.distance

try:
    detector_range = gamlib.string_to_2dlist(args.range)
except Exception as e:
    print "Error converting input range into tuple. Please check the sanity of your input."
    print "Error message: ", e
    exit(1)

print
print detector_range
print

# Calculated constants
frequency = 1 / mean_lifetime

# Lifetimes follow Poisson distribution with mean 520 microseconds

print "Simulating random decay positions..."
lifetimes, decay_positions = gamlib.simulate_decay_positions(frequency, args.speed, num_decays)

dists_from_detector = inj_to_det_dist - decay_positions
print "...done\n"

print "Simulating random angles..."
phi, theta = gamlib.produce_angles(num_decays)
print "...done\n"

print "Calculating detector positions..."
x_pos, y_pos = gamlib.calculate_detector_positions(phi, theta, dists_from_detector)
print "...done\n"

print "Plotting decay times and positions to eps file..."
gamplt.plot_times_and_distances(lifetimes, decay_positions)
print "...done\n"

print "Plotting decay angles to eps file..."
gamplt.plot_decay_angles(phi, theta)
print "...done\n"

print "Plotting detector readings to eps file..."
detector_range = ((-2.5,2.5),(-2.5,2.5))
gamplt.plot_detector(x_pos, y_pos, detector_range)
print "...done"
