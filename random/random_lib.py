from __future__ import division

# In-built libraries
import sys
import random
import math

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

def reject_accept(num):
    # Use reject-accept method to produce random numbers distributed as 
    # sin(theta) in 0 < theta < pi

    first = np.random.uniform(0,math.pi,num)
    second = np.random.uniform(0,1,num)

    criterion = second < np.sin(first)

    sinusoid = filter(lambda i: criterion[i], first)

    print "Sinusoidal random number distribution using reject-accept method produced."

    return sinusoid

def display_progress(current, target):
    # Displays progress bar showing how close current is to target

    percentage = 100*(current+1)/target

    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))

    return 0
