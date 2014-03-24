from math import pi,e

# Messy, but necessary for the any function random distributor
from numpy import *

def string_to_function(string):
    # Turn string taken from argument into function to produce random distribution around

    print "<lambda> string: ", string
    func = lambda x: eval(string)

    return func
