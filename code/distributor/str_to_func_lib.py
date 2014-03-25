from __future__ import division

from math import pi,e
from scipy.special import lambertw

# Messy, but necessary for the any function random distributor
from numpy import *

# Custom libraries
import distributor_lib as dstlib

def string_to_function(string):
    # Turn string taken from argument into function to produce random distribution around

    print "<lambda> string: ", string
    func = lambda x: eval(string)

    print
    dstlib.debug_var(__name__, "func(0)", func(0))
    print

    return func
