from __future__ import division

# In-built libraries
import time
import argparse

# Custom libraries
import analytic_sin_lib as analib
import analytic_sin_io as anaio

try:
    import analytic_sin_plot as anaplt 
    can_plot = True
except ImportError as e:
    print "[Error] Error importing plotting library; plotting functions ('-p'/'--plot') will be unavailable."
    print "[Error] Error message:", e, "\n"
    can_plot = False

parser = argparse.ArgumentParser(description="Producing random numbers distributed as sin(theta)")

parser.add_argument("-p", "--plot", action="store_true",
                    help="Plots resulting random distributions to file.")

parser.add_argument("-o", "--output",
                    help="Write resulting output random numbers to file.")

parser.add_argument("-n", "--num", type=float, default=1e6,
                    help="Number of initial random numbers to produce. This will equal the number"\
                         " of sinusoidally distributed random numbers.")

parser.add_argument("-t", "--timed", action="store_true",
                    help="Time operations for performance comparison.")

parser.add_argument("-x", "--excel",
                    help="Write resulting output random numbers to excel spreadsheet.")

# Arguments go here, once I've finalised and decided what they are

args = parser.parse_args()

# If you want to plot but can't, print message and prevent from trying to plot
if not can_plot and args.plot:
    print "[Warning] Plotting disabled due to import error.\n"
    args.plot = False

num = int(args.num) # This means scientific notation can be accepted as argument

start = time.clock()
even = analib.produce_randoms(num)
end = time.clock()
if args.timed:
    print "[ Processor time taken:", end - start, "]"
print

# Analytic convert evenly distributed random numbers into sinusoidally
# distributed ones

start = time.clock()
analytic_sin = analib.trans_to_sin(even)
end = time.clock()
if args.timed:
    print "[ Processor time taken:", end - start, "]"
print

# Plot output to eps file

if args.plot:
    print "Plotting random sinusoidal distribution..."
    anaplt.plot_hist(analytic_sin, title="Analytically Generated Random Sin Distribution",
                     fname="analytic_sin")
    print "...done\n"

# Write output to file

if args.output:
    start = time.clock()

    print "Writing random distribution to file..."
    anaio.output_to_file(analytic_sin, args.output)
    print "...done\n"

    end = time.clock()
    if args.timed:
        print "[ Processor time taken:", end - start, "s ]"
    print

# Write output to Excel spreadsheet

if args.excel:
    start = time.clock()

    print "Writing random distribution data to Excel spreadsheet..."
    start = time.clock()
    anaio.output_to_excel(analytic_sin, args.excel)
    print "...done"

    end = time.clock()
    if args.timed:
        print "[ Processor time taken:", end - start, "s ]"
