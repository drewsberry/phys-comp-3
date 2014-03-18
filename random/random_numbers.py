from __future__ import division

# In-built libraries
import time

# External libraries
import numpy as np
import matplotlib.pyplot as plt

# Custom libraries
import random_lib as rndlib
import random_plot as rndplt

num_numbers = int(1e6)

start = time.clock()

even = rndlib.produce_randoms(num_numbers)

end = time.clock()
print "Time taken: ", end - start
print

# Analytic method

start = time.clock()

sinusoid = rndlib.trans_to_sin(even)

end = time.clock()

print
print "Time taken: ", end - start
print

rndplt.plot_sin_hist(sinusoid)

# Reject-accept method

