from __future__ import division

import random as rnd
import math
import sys
import time

import numpy as np
import matplotlib.pyplot as plt

rnd.seed()
# Set seed from current system time

rand = rnd.SystemRandom()
# Use system pseudo-random numbers

num_numbers = int(1e6)
even = []
start = time.clock()
print "Random numbers produced: ",
for i in range(num_numbers):
    even.append(rand.random())
    percentage = 100*(i+1)/num_numbers
    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))
end = time.clock()
print
print "Time taken: ", end - start

print "Initial even random number distribution produced"

## Analytic method

sinusoid = []
start = time.clock()
print "Co-ordinate transformations completed: ",
for i in range(num_numbers):
    sinusoid.append(math.acos(1 -even[i]))
    percentage = 100*(i+1)/num_numbers
    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))
end = time.clock()
print
print "Time taken: ", end - start

print "Sinusoidal random number distribution using analytic method produced"

fig, ax1 = plt.subplots()

num_bins = 100
bin_width = (math.pi/2) / num_bins

n, bins, pathes = ax1.hist(sinusoid, num_bins, color="red")

x = np.arange(0, math.pi/2, 0.1)
l = ax1.plot(x, num_numbers*bin_width*np.sin(x), linewidth=5)
plt.show()
