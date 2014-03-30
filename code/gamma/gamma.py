from __future__ import division

# In-built libraries
import time
import argparse

# Custom libraries
import gamma_lib as gamlib
try:
    import gamma_plot as gamplt
    can_plot = True
except ImportError as e:
    print "[Warning] Error importing plotting library; plotting functions ('-p'/'--plot') will be unavailable."
    print "[Warning] Error message:", e, "\n"
    can_plot = False

parser = argparse.ArgumentParser(description="Simulating the decay of injected nuclei travelling towards a detector.")

parser.add_argument("-r", "--range", default="((5,5),(5,5))",
                    help="range of detector. Enter as python tuple in string form without spaces, e.g. '((-5,5),(-5,5))'")

parser.add_argument("-n", "--num", type=float, default=1e7,
                    help="The number of decays to simulate.")

parser.add_argument("-s", "--speed", type=float, default=2000,
                    help="Speed of injected unstable nuclei, in meters per second.")

parser.add_argument("-l", "--lifetime", type=float, default=520,
                    help="Average lifetime of unstable nucleus, in microseconds.")

parser.add_argument("-xr", "--xres", type=float, default=10,
                    help="x resolution of detector in centimetres,")

parser.add_argument("-yr", "--yres", type=float, default=30,
                    help="y resolution of detector in centimetres,")

parser.add_argument("-d", "--distance", type=float, default=2,
                    help="distance from injection point to detector, in meters.")

parser.add_argument("-p", "--plot", action="store_true",
                    help="Plot resulting simulation data to graphs as eps files.")

parser.add_argument("-t", "--timed", action="store_true",
                    help="Print processor timings for each step for purposes of performance analysis.")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="Increase verbosity; print out additional information such as progress bars (slows down program).")

args = parser.parse_args()

# If you want to plot but can't, print message and prevent from trying to plot
if not can_plot and args.plot:
    print "[Warning] Plotting disabled due to import error.\n"
    args.plot = False

num_decays = int(args.num)
mean_lifetime = args.lifetime*1e-6 # microseconds
res_x = args.xres / 100 # cm -> m
res_y = args.yres / 100 # cm -> m
inj_to_det_dist = args.distance
frequency = 1 / mean_lifetime

try:
    detector_range = gamlib.string_to_2dlist(args.range)
except Exception as e:
    print "Error converting input range into tuple. Please check the sanity of your input."
    print "Error message:", e
    exit(10)


start = time.clock()
print "Simulating random decay positions..."
lifetimes, decay_positions = gamlib.simulate_decay_positions(frequency, args.speed, num_decays)

dists_from_detector = inj_to_det_dist - decay_positions
print "...done"
end = time.clock()
if args.timed:
    print "[ Processor time taken for random decay simulation:", end - start, "s ]"
print

start = time.clock()
print "Simulating random angles..."
phi, theta = gamlib.produce_angles(num_decays)
print "...done"
end = time.clock()
if args.timed:
    print "[ Processor time taken for random angle simulation:", end - start, "s ]"
print

start = time.clock()
print "Calculating detector positions..."
x_pos, y_pos = gamlib.calculate_detector_positions(phi, theta, dists_from_detector)
print "...done"
end = time.clock()
if args.timed:
    print "[ Processor time taken for detector positions calculation:", end - start, "s ]"
print

start_total = time.clock()
print "Smearing detector positions to simulate detector resolution...\n"

start = time.clock()
x_pos_smeared = gamlib.smear(x_pos, res_x, args.verbose)
print "...x positions smeared..."
end = time.clock()
if args.timed:
    print "[ Processor time taken for x smearing:", end - start, "s ]"
print

start = time.clock()
y_pos_smeared = gamlib.smear(y_pos, res_y, args.verbose)
print "...y positions smeared..."
end = time.clock()
if args.timed:
    print "[ Processor time taken for y smearing:", end - start, "s ]"
print

print "...done"
end_total = time.clock()
if args.timed:
    print "[ Total processor time taken for smearing:", end_total - start_total, "s ]"
print

if args.plot:
    start = time.clock()
    print "Plotting decay times and positions to eps file..."
    gamplt.plot_times_and_distances(lifetimes, decay_positions)
    print "...done"
    end = time.clock()
    if args.timed:
        print "[ Processor time taken for plotting decay times and positions:", end - start, "s ]"
    print

    start = time.clock()
    print "Plotting decay angles to eps file..."
    gamplt.plot_decay_angles(phi, theta)
    print "...done"
    end = time.clock()
    if args.timed:
        print "[ Processor time taken for histogramming decay angles:", end - start, "s ]"
    print

    start = time.clock()
    print "Plotting unsmeared detector readings to eps file..."
    gamplt.plot_detector(x_pos, y_pos, detector_range, res_x, res_y,
                         title="Unsmeared $\gamma$ Ray Detector Readings",
                         fname="gamma_detector_unsmeared")
    print "...done"
    end = time.clock()
    if args.timed:
        print "[ Processor time taken for histogramming unsmeared detector readings:", end - start, "s ]"
    print

    start = time.clock()
    print "Plotting smeared detector readings to eps file..."
    gamplt.plot_detector(x_pos_smeared, y_pos_smeared, detector_range, res_x, res_y,
                         title="Smeared $\gamma$ Ray Detector Readings",
                         fname="gamma_detector_smeared")
    print "...done"
    end = time.clock()
    if args.timed:
        print "[ Processor time taken for histogramming smeared detector readings:", end - start, "s ]"
