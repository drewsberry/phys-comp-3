from __future__ import division

# In-built libraries
import time
import argparse

# External libraries
import numpy as np
import matplotlib.pyplot as plt

# Custom libraries
import random_lib as rndlib
import random_plot as rndplt

parser = argparse.ArgumentParser(description="Producing random numbers distributed as sin(theta)")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="Increase verbosity; print information including progress bars - slows"\
                         " down program.")

parser.add_argument("-p", "--plot", action="store_true",
                    help="Plots resulting random distributions to file.")

parser.add_argument("-o", "--output",
                    help="Write resulting output random numbers to file.")

parser.add_argument("-n", "--num", type=float, default=1e6,
                    help="Number of initial random numbers to produce. This will equal the number"\
                         " of sinusoidally distributed random numbers for the analytic method, but"\
                         " not for the reject-accept method unless the '-f'/'--fixnum' flags are"\
                         " also used.")

parser.add_argument("-f", "--fixnum", action="store_true",
                    help="Produce fixed number of random sinusoidally distributed numbers.")

parser.add_argument("-t", "--timed", action="store_true",
                    help="Time operations for performance comparison.")

# Arguments go here, once I've finalised and decided what they are

args = parser.parse_args()

num = int(args.num) # This means scientific notation can be accepted as argument

start = time.clock()
even = rndlib.produce_randoms(num)
end = time.clock()
if args.timed:
    print "Processor time taken: ", end - start
print

# Analytic method

start = time.clock()
analytic_sin = rndlib.trans_to_sin(even)
end = time.clock()
if args.timed:
    print "Processor time taken: ", end - start
print

# Reject-accept method

if not args.fixnum:
    start = time.clock()
    reject_accept_sin = rndlib.reject_accept_sin(num, args.verbose)
    end = time.clock()
    if args.timed:
        print "Processor time taken: ", end - start
    print

# Fixed reject-accept method

if args.fixnum:
    start = time.clock()
    reject_accept_sin = rndlib.reject_accept_sin_fixed(num, args.verbose)
    end = time.clock()
    if args.timed:
        print "Processor time taken: ", end - start
    print

if args.plot:
    rndplt.plot_sin_hist(analytic_sin, title="Analytic Method", fname="analytic")
    rndplt.plot_sin_hist(reject_accept_sin, title="Reject-Accept Method", fname="reject_accept")
