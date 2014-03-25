from __future__ import division

# In-built libraries
import sys
import random
import math
import re
from math import pi,e

# External libraries
import numpy as np

# Custom libraries
import str_to_func_lib as stfl

# rnd = random.SystemRandom()
## Use system produced random numbers

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

    # tuple = tuple(int(x) for x in re.findall("[0-9]+", string))

    lst = string.lstrip("(").rstrip(")").split(",")
    # Remove bracket "(", ")" and comma "," and split elements into list

    lst = map(eval, lst)
    # Convert all members from strings to floats

    return lst

def reject_accept(num, verb, func_str, dist_range):
    # Use reject-accept method to produce random numbers distributed as 
    # general user-defined function in user-defined range

    func = stfl.string_to_function(func_str)

    print "<reject_accept> func_str: ", func_str
    print "<reject_accept> func: ", func

    print "<reject_accept> func(0):", func(2)

    print "<reject_accept> dist_range, type(dist_range): ", dist_range, type(dist_range)

    first = np.random.uniform(dist_range[0],dist_range[1],num)
    second = np.random.uniform(0,func(dist_range[1]),num)
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

    print "done"

    if verb:
        print "{} random numbers produced.".format(len(dist))

    return dist 

def reject_accept_fixed(num, verb, func_str, dist_range):
    # Use reject-accept method to produce fixed number of random numbers
    # distributed as per user-defined function

    func = stfl.string_to_function(func_str)

    # The 5 is just because chance if I produce 9 times the number I need then
    # chances are at that I'll get at least num out (specifically, 1*num produces
    # about 0.6*num out, so 9*num is insufficient in ~1% of all runs). There is a 
    # trade-off here in terms of efficiency and processing time.
    first = np.random.uniform(dist_range[0],dist_range[1],9*num)
    second = np.random.uniform(0,func(dist_range[1]),9*num)
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
                print "done"

                return dist 
        if verb:
            display_progress(len(dist),num)

    return False
