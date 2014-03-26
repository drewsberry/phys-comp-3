from __future__ import division

# In-built libraries
import sys
from math import pi,e # So that pi or e can be used in range

# External libraries
import numpy as np

# Custom libraries
import str_to_func_lib as stfl

def display_progress(current, target):
    # Displays progress bar showing how close current is to target

    percentage = 100*(current+1)/target

    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))
        if percentage == 100:
            print

    return 0

def string_to_list(string):
    # Turn string into list so range can be parsed by arguments neatly and intuitively

    lst = string.lstrip("(").rstrip(")").split(",")
    # Remove bracket "(", ")" and comma "," and split elements into list

    lst = map(eval, lst)
    # Convert all members from strings to floats

    return lst

def reject_accept(num, verb, func_str, dist_range):
    # Use reject-accept method to produce random numbers distributed as 
    # general user-defined function in user-defined range

    func = stfl.string_to_function(func_str)

    func_max = find_max(func, dist_range)

    first = np.random.uniform(dist_range[0], dist_range[1], num)
    second = np.random.uniform(0, func_max, num)
    dist = []

    criterion = second < func(first)

    print "Producing random user-distributed numbers using reject-accept method...",

    if verb:
        print
        print "Random numbers produced:",

    for i in range(num):
        if criterion[i]:
            dist.append(first[i])
        if verb:
            display_progress(i+1,num)

    if verb:
        print "...",
    print "done"

    if verb:
        print "{} random numbers produced.".format(len(dist))

    return dist 

def reject_accept_fixed(num, verb, func_str, dist_range):
    # Use reject-accept method to produce fixed number of random numbers
    # distributed as per user-defined function

    func = stfl.string_to_function(func_str)

    func_max = find_max(func, dist_range)

    # The 5 is just because chance if I produce 9 times the number I need then
    # chances are at that I'll get at least num out (specifically, 1*num produces
    # about 0.6*num out, so 9*num is insufficient in ~1% of all runs). There is a 
    # trade-off here in terms of efficiency and processing time.
    first = np.random.uniform(dist_range[0], dist_range[1], 9*num)
    second = np.random.uniform(0, func_max, 9*num)
    dist = []

    criterion = second < func(first)

    print "Producing fixed number {} of random user-distributed numbers "\
          "via reject-accept method...".format(num),

    if verb:
        print
        print "Random numbers produced: ",

    for i in range(len(criterion)):
        if criterion[i]:
            dist.append(first[i])
            if len(dist) >= num:
                if verb:
                    print "...",
                print "done"

                return dist 
        if verb:
            display_progress(len(dist),num)

    print "Error generating random distribution using fixed reject-accept method."
    return False

def find_max(function, fc_range):
    # Find maximum value of function in dist_range

    delta_x = 0.1

    dist = function(np.arange(fc_range[0], fc_range[1], delta_x))

    return np.max(dist)
