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

analytic_sin = rndlib.trans_to_sin(even)

end = time.clock()

print "Time taken: ", end - start
print

# Reject-accept method

start = time.clock()
reject_accept_sin = rndlib.reject_accept(num_numbers)
end = time.clock()
print "Time taken: ", end - start
print

rndplt.plot_sin_hist(reject_accept_sin, title="Reject-Accept Method", fname="reject_accept")
rndplt.plot_sin_hist(analytic_sin, title="Analytic Method", fname="analytic")
