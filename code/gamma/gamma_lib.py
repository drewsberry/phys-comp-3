from __future__ import division

# In-built libraries
import sys

# External libraries
import numpy as np

def simulate_decay_positions(frequency, speed, num):
    # Simulate num decays using Poisson distribution, and return the an array of the lifetimes and decay positions from injection point of the nuclei.

    # Lifetimes follow Poisson distribution with mean num events per sec 1/520e-6
    num_events_per_sec = np.random.poisson(frequency, num)

    # Time is reciprocal of frequency
    lifetimes = 1 / num_events_per_sec

    # Distance is time*speed
    decay_positions = lifetimes*speed

    return lifetimes, decay_positions

def produce_angles(num):
    # Produce num spherical angles, avoiding clumping

    # phi is even on interval (0, 2*pi)
    phi = 2*np.pi*np.random.random(num)

    # theta is sinusoidallu distributed on interval (0, pi), cf. analytic sin distribution
    theta = np.arccos(2*np.random.random(num) - 1)

    # Ensures theta points towards detector; essential for calculation of y in calculating detector positions
    theta -= np.pi/2

    return phi, theta

def calculate_detector_positions(phi, theta, dists_from_detector):
    # use trigonometry to find x and y positions on detector

    # From trigonometry; explained in detail in report
    x = dists_from_detector*np.tan(phi)
    y = dists_from_detector*np.tan(theta) / np.cos(phi)

    return x, y

def string_to_2dlist(string):
    # Convert string to 2d list for detector size input

    # Split into x and y range portions
    range_x, range_y = string.split("),(")

    # Remove leading and trailing parentheses
    range_x = range_x.lstrip("((").split(",")
    range_y = range_y.rstrip("))").split(",")

    # map strings to ints
    lst2d = (map(float, range_x), map(float, range_y))

    return lst2d

def smear(positions, resolution, verb):
    # Apply Gaussian smearing to bins with mean 'mean' and standard deviation 'sigma'

    smeared_positions = np.copy(positions)
    num = len(smeared_positions)

    if verb:
        print "Positions smeared:"

    for i in xrange(num):
        smeared_positions[i] += np.random.normal(loc=smeared_positions[i], scale=resolution)
        if verb:
            display_progress(i, num)

    return smeared_positions 

## Probably don't need this
def round_to_res(number, res):
    # Round 'number' to resolution of detector (i.e. res_x or res_y), 'res'
    rounded = res * round(number / res)

    # Always returns float
    return rounded

def display_progress(current, target):
    # Displays progress bar showing how close current is to target

    percentage = 100*(current+1)/target

    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))
        if percentage == 100:
            print

    return 0
