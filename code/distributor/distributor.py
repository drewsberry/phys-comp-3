from __future__ import division

# In-built libraries
import time
import argparse

# Custom libraries
import distributor_lib as dstlib 
import str_to_func_lib as stflib
import distributor_io as dstio

try:
    import distributor_plot as dstplt 
    can_plot = True
except ImportError as e:
    print "[Warning] Error importing plotting library; plotting functions ('-p'/'--plot') will be unavailable."
    print "[Warning] Error message:", e, "\n"
    can_plot = False

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

parser.add_argument("-p", "--plot", action="store_true",
                    help="plots resulting random distributions to file.")

parser.add_argument("-o", "--output",
                    help="Write resulting output random numbers to file.")

parser.add_argument("-x", "--excel",
                    help="Write resulting output random numbers to excel spreadsheet.")

parser.add_argument("-n", "--num", type=float, default=1e6,
                    help="number of initial random numbers to produce. This will not equal the number"\
                         " of user-distributed random numbers unless unless the '-f'/'--fixnum'"\
                         " flags are used.")

parser.add_argument("-f", "--fixnum", action="store_true",
                    help="produce fixed number of random user-distributed numbers.")

parser.add_argument("-t", "--timed", action="store_true",
                    help="time operations for performance comparison.")

args = parser.parse_args()

# If you want to plot but can't, print message and prevent from trying to plot
if not can_plot and args.plot:
    print "[Warning] Plotting disabled due to import error.\n"
    args.plot = False

num = int(args.num) # This means scientific notation (float) can be accepted in argument

try:
    dist_range = dstlib.string_to_list(args.range)
except Exception as e:
    print "[Error] Error converting input range into list."\
          " Please check the sanity of your input."
    print "[Error] Error message:", e
    exit(10)

try:
    function = stflib.string_to_function(args.func)
except Exception as e:
    print "[Error] Error converting input function string into Python function."\
          " Please check the sanity of your input."
    print "[Error] Error message:", e
    exit(20)

# Reject-accept method

if not args.fixnum:
    start = time.clock()
    print "Producing random user-distributed numbers using reject-accept method..."
    random_dist = dstlib.reject_accept(num, args.func, dist_range)
    print "...done"
    end = time.clock()
    if args.timed:
        print "[ Processor time taken:", end - start, "s ]"
    print

# Fixed reject-accept method

if args.fixnum:
    start = time.clock()
    print "Producing fixed number {} of random user-distributed numbers "\
          "via reject-accept method...".format(num)
    random_dist = dstlib.reject_accept_fixed(num, args.func, dist_range)
    print "...done"
    end = time.clock()
    if args.timed:
        print "[ Processor time taken:", end - start, "s ]"
    print

if args.plot:
     dstplt.plot_hist(random_dist, args.func, dist_range,
                      # title=args.func+" Distribution, Reject-Accept Method",
                      title="Reject-Accepted Generated Random Sin Distribution ($10^8$ numbers)",
                      fname="reject_accept")

# Write output to file

if args.output:
    start = time.clock()

    print "Writing random distribution to file..."
    dstio.output_to_file(random_dist, args.output, args.func)
    print "...done"

    end = time.clock()
    if args.timed:
        print "[ Processor time taken:", end - start, "s ]"
    print

# Write output to Excel spreadsheet

if args.excel:
    start = time.clock()

    print "Writing random distribution data to excel spreadsheet..."
    start = time.clock()
    dstio.output_to_excel(random_dist, args.excel, args.func)
    print "...done"

    end = time.clock()
    if args.timed:
        print "[ Processor time taken:", end - start, "s ]"
