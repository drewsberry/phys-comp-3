from __future__ import division

# In-built libraries
import time
import argparse

# External libraries
import numpy as np
import matplotlib.pyplot as plt

# Custom libraries
import distributor_lib as dstlib 
import distributor_plot as dstplt 
import str_to_func_lib as stfl
import random_io as rndio

parser = argparse.ArgumentParser(description="Producing random numbers distributed as per user"\
                                             " input function.")

parser.add_argument("func", help="the function to distribute randomly around. All mathematical"\
                                 " functions supported by NumPy nad SciPy's special functions are"\
                                 " valid, with the caveat that functions returning complex arguments"\
                                 " will be forced into real values and functions returning 2d arrays"\
                                 " (e.g. scipy.special.airy) are unsupported. Enter as string, "\
                                 " e.g. 'sin(x)'.")

parser.add_argument("-r", "--range", required=True,
                    help="the range to produce random numbers from and to. Enter as string"\
                         " tuple, e.g. '(0,pi)'")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase verbosity; print additional information including progress bars"\
                         " (slows down program).")

parser.add_argument("-p", "--plot", action="store_true",
                    help="plots resulting random distributions to file.")

parser.add_argument("-o", "--output",
                    help="Write resulting output random numbers to file.")

parser.add_argument("-e", "--excel",
                    help="Write resulting output random numbers to excel spreadsheet.")

parser.add_argument("-n", "--num", type=float, default=1e6,
                    help="number of initial random numbers to produce. This will equal the number"\
                         " of sinusoidally distributed random numbers for the analytic method, but"\
                         " not for the reject-accept method unless the '-f'/'--fixnum' flags are"\
                         " also used.")

parser.add_argument("-f", "--fixnum", action="store_true",
                    help="produce fixed number of random sinusoidally distributed numbers.")

parser.add_argument("-t", "--timed", action="store_true",
                    help="time operations for performance comparison.")

args = parser.parse_args()

num = int(args.num) # This means scientific notation (float) can be accepted in argument
dist_range = dstlib.string_to_list(args.range)

# Reject-accept method

if not args.fixnum:
    start = time.clock()
    random_dist = dstlib.reject_accept(num, args.verbose, args.func, dist_range)
    end = time.clock()
    if args.timed:
        print "Processor time taken: {} s".format(end - start)
    print

# Fixed reject-accept method

if args.fixnum:
    start = time.clock()
    random_dist = dstlib.reject_accept_fixed(num, args.verbose, args.func, dist_range)
    end = time.clock()
    if args.timed:
        print "Processor time taken: {} s".format(end - start)
    print

if args.plot:
     dstplt.plot_gen_hist(random_dist, title=args.func+" Distribution, Reject-Accept Method", 
                         fname="reject_accept", func_str=args.func, plot_range=dist_range)

# Write output to file

if args.output:
    start = time.clock()

    print "Writing random distribution to file...",
    rndio.output_to_file(random_dist, args.output, args.func)
    print "done"

    end = time.clock()
    if args.timed:
        print "Processor time taken: {} s".format(end - start)
    print

# Write output to Excel spreadsheet

if args.excel:
    start = time.clock()

    print "Writing random distribution data to excel spreadsheet...",
    start = time.clock()
    rndio.output_to_excel(random_dist, args.excel, args.func)
    print "done"

    end = time.clock()
    if args.timed:
        print "Processor time taken: {} s".format(end - start)
