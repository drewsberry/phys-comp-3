# distributor

This directory contains the script and libraries for the general reject-accept distributor.

The actual file to run is 'distributor.py'

The other files are as follows:
    - distributor_lib.py: library containing most of the function calls used as part of the program.
    - distributor_plot.py: library containing the plotting functions (optional; works without matplotlib but with plotting disabled).
    - distributor_io.py: library containing the input/output functions used by distributor.py, namely write to output file and write to Excel spreadsheet if you have xlwt installed.
    - str_to_func_lib.py: library containing function that takes string from argument as input and returns a lambda function that evaluates the equation specified by the user. Note the 'from {numpy, scipy.special} import *' statements. These are so the user need not input "np.sin(x)", which they shouldn't have to.

Subdirectories are the default locations to save data and graphs.

distributor.py options:
    - "func": Main positional (compulsory) argument; a string that when evaluated is a valid Python expression, e.g. "sin(x)", "gamma(x)" etc.
    - -r/--range: The range to produce random numbers from and to. Required argument. Enter as tuple inside a string, e.g. "(-1,2)", "(-e,pi)" etc.
    - -p/--plot: Plot to file.
    - -o/--output: Output random data to file.
    - -x/--excel: Output random data to Excel spreadsheet if xlwt is installed.
    - -n/--num: The number of initial random numbers to generate. Not guaranteed to be same as produced number due to *reject*-accept method, unless -f/--fixnum is chosen, in which I go to extra effort to make sure you do produce num numbers.
    - -f/--fixnum: Produce a fixed number of random numbers as output.
    - -t/--timed: Time each operation for debugging/performance comparison purposes.
