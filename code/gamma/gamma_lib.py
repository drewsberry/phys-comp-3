from __future__ import division

import numpy as np

def simulate_decay_positions(frequency, speed, num):
    # Simulate num decays using Poisson distribution, and return the an array of the lifetimes of the nuclei.

    num_events_per_sec = np.random.poisson(frequency, num)

    lifetimes = 1 / num_events_per_sec

    decay_positions = lifetimes*speed

    return lifetimes, decay_positions

def produce_angles(num):
    # Produce num spherical angles, avoiding clumping

    phi = 2*np.pi*np.random.random(num)
    theta = np.arccos(2*np.random.random(num) - 1)

    theta -= np.pi/2

    return phi, theta

def calculate_detector_positions(phi, theta, dists_from_detector):
    # use trigonometry to find x and y positions on detector

    x = dists_from_detector*np.tan(phi)
    y = dists_from_detector*np.tan(theta) / np.cos(phi)

    return x, y

def string_to_2dlist(string):
    # Convert string to 2d list for detector size input

    range_x, range_y = string.split("),(")

    range_x = range_x.lstrip("((")
    range_y = range_y.rstrip("))")

    lst2d = (eval(range_x), eval(range_y))

    return lst2d
