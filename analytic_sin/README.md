# analytic_sin

This directory contains the script and libraries for the analytic sin inverter.

The actual file to run is 'analytic_sin.py'.

The other files are as follows:
    - analytic_sin_lib.py: (small) library for analytic_sin.py containing random number production and analytic conversion functions.

    - analytic_sin_plot.py: library containing plotting functions for analytic_sin.py. Used to plot histograms of random distribution using matplotlib (optional; it works without having matplotlib installed, it just loses the capacity to plot to graph.)

    - analytic_sin_io.py: library containing input output functions, such as print data to file and print data to Excel spreadsheet (if xlwt is installed).

Subdirectories are the default locations to save data and graphs.

analytic_sin.py options:
    - -p/--plot: Plot to file.
    - -o/--output: Print random data to file.
    - -n/--num: Number of random numbers to produce.
    - -t/--timed: Print processor timing information.
    - -x/--excel: Print data to Excel spreadsheet. Note a limitation in Excel before 2007 that the number of rows cannot exceed 65536.

Note that no arguments need be specified. Giving no arguments does not plot or print output, but works fine.
