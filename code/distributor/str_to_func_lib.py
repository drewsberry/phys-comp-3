from __future__ import division

from math import pi,e

# Messy, but necessary so that user need not input "np.sin", "np.arcsin" etc.
from numpy import *
from scipy.special import *

def string_to_function(string):
    # Turn string taken from argument into function to produce random distribution around

    func = lambda x: eval(string)

    return func
