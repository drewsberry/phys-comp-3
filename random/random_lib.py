from __future__ import division

# In-built libraries
import sys
import random

# External libraries
import numpy as np

rnd = random.SystemRandom()
# Use system produced random numbers

def produce_randoms(num):
    # Produce num evenly distributed random numbers 

    even = np.random.uniform(0,2,num)

    print "Initial even random number distribution produced."

    return even

def trans_to_sin(even):
    # Translate evenly distributed random numbers to those distributed as 
    # sin(theta) in 0 < theta < pi

    num = len(even)

    sinusoid = np.arccos(1 - even)

    print "Sinusoidal random number distribution using analytic method produced."

    return sinusoid
