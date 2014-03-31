from __future__ import division

# In-built libraries
import sys
from math import pi,e # So that pi or e can be used in range

# External libraries
import numpy as np

# Custom libraries
import str_to_func_lib as stfl

def string_to_list(string):
    # Turn string into list so range can be parsed by arguments neatly and intuitively

    lst = string.lstrip("(").rstrip(")").split(",")
    # Remove bracket "(", ")" and comma "," and split elements into list

    lst = map(eval, lst)
    # Convert all members from strings to floats, evaluating pi and e

    return lst

def reject_accept(num, func_str, dist_range):
    # Use reject-accept method to produce random numbers distributed as 
    # general user-defined function in user-defined range

    func = stfl.string_to_function(func_str)

    func_max = find_max(func, dist_range)

    # First random variables, x', evenly generated in range
    first = np.random.uniform(dist_range[0], dist_range[1], num)

    # Second random variables, y, evenly generated in [0, y_max]
    second = np.random.uniform(0, func_max, num)

    # If second random variable, y, is less than P'(x'), accept it.
    criterion = second < func(first)

    # dist is all values of first with corresponding True criterion
    dist = first[criterion]

    print "{} random numbers produced.".format(len(dist))

    return dist 

def reject_accept_fixed(num, func_str, dist_range):
    # Use reject-accept method to produce fixed number of random numbers
    # distributed as per user-defined function

    func = stfl.string_to_function(func_str)

    func_max = find_max(func, dist_range)

    # The 9* is just because if I produce 9 times the number I need then
    # chances are increased from ~40% for 1*num to about ~99% that I will
    # produce sufficient user-distributed numbers.

    # First random variables, x', evenly generated in range
    first = np.random.uniform(dist_range[0], dist_range[1], 9*num)

    # Second random variables, y, evenly generated in [0, y_max]
    second = np.random.uniform(0, func_max, 9*num)

    # If second random variable, y, is less than P'(x'), accept it.
    criterion = second < func(first)

    try:
        # dist is all values of first with corresponding True criterion,
        # choosing only the first 'num' of them
        dist = first[criterion][0:num]
        return dist
    except IndexError as e:
        print "[Error] Error generating random distribution using fixed reject-accept method:"
        print "[Error] Insufficient random numbers produced. Please try again."
        return False

def find_max(function, fc_range):
    # Find maximum value of function in dist_range

    delta_x = 0.0001

    # Apply function to array of numbers delta_x apart in given range, and find max value
    dist = function(np.arange(fc_range[0], fc_range[1], delta_x))

    return np.max(dist)
