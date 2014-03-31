# gamma

This directory contains the script for the Monte Carlo detector simulation, as well as a small script to run a pretty and fun interactive visualisation of how clumping forms when points are not properly picked on a sphere.

The actual file to run is 'gamma.py', and the Mayavi visualisation is 'sphere_mayavi.py'.

The other files are as follows:
    - gamma_lib.py: library containing functions used by gamma.py for Monte Carlo simulation.
    - gamma_plot.py: library containing functions for plotting the various output results form the simulation.
    - sphere_mayavi_lib.py: library containing functions sued by sphere_mayavi.py for the running of the sphere visualisations. Requires mayavi2 to run (runs 'from mayavi import mlab').

Subdirectories are the default locations to save data and graphs.

gamma.py options:
    - -r/--range: Size of detector in meters. Enter as tuple inside string, e.g. "((-2.5,2.5),(-4.5,4.5))" would plot for a detector from -2.5 to 2.5 in X direction and from -4.5 to 4.5 in Y direction. Note that there should be no spaces in the string.
    - -n/--num: Number of decays to simulate. Default is 10 million.
    - -s/--speed: Speed of injected nuclei in meters per second. Default is 2000.
    - -l/--lifetime: Average lifetime of nucleus in microseconds. Default is 520.
    - -xr/--xres: x-resolution of detector in centimetres. Used for both binning and smearing. Default is 10.
    - -yr/--yres: y-resolution of detector in centimetres. Used for both binning and smearing. Default is 30.
    - -d/--distance: Distance from point of injection to detector.
    - -p/--plot: Plot resulting simulated data to eps files.
    - -t/--timed: Print processor clock timing information for performance analysis/debugging.

Note that gamma.py runs fine without any of the optional arguments, as it's set by default to all the values specified in the script, with a range of -5 to 5 in both X and Y.

sphere_mayavi.py has no options because it's just a straight script.
