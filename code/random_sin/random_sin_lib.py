# In-built libraries
import math

#External libraries
import numpy as np

def produce_randoms(num):
    # Produce num evenly distributed random numbers 

    print "Producing {} uniformly distributed random numbers... ".format(num),
    even = np.random.uniform(0,2,num)
    print "done"

    return even

def trans_to_sin(even):
    # Translate evenly distributed random numbers to those distributed as 
    # sin(theta) in 0 < theta < pi

    num = len(even)

    print "Analytically transforming {} evenly distributed random numbers to "\
          "sinusoidally distributed ones...".format(num),
    sinusoid = np.arccos(1 - even)
    print "done"

    return sinusoid

def reject_accept_sin(num, verb):
    # Use reject-accept method to produce random numbers distributed as 
    # sin(theta) in 0 < theta < pi

    first = np.random.uniform(0,math.pi,num)
    second = np.random.uniform(0,1,num)
    sinusoid = []

    criterion = second < np.sin(first)

    print "Producing random sinusoidally distributed numbers using reject-accept method...",

    if verb:
        print
        print "Random numbers produced:",

    for i in range(num):
        if criterion[i]:
            sinusoid.append(first[i])
        if verb:
            display_progress(i+1,num)

    print "done"

    if verb:
        print "{} random numbers produced.".format(len(sinusoid))

    return sinusoid
    
def reject_accept_sin_fixed(num, verb):
    # Use reject-accept method to produce fixed number of random sinusoidally 
    # distributed numbers

    # The 5 is just because chance if I produce 9 times the number I need then
    # chances are at that I'll get at least num out (specifically, 1*num produces
    # about 0.6*num out, so 9*num is insufficient in ~1% of all runs). There is a 
    # trade-off here in terms of efficiency and processing time.
    first = np.random.uniform(0,math.pi,9*num)
    second = np.random.uniform(0,1,9*num)
    sinusoid = []

    criterion = second < np.sin(first)

    print "Producing fixed number {} of random sinusoidally distributed numbers "\
          "via reject-accept method...".format(num),

    if verb:
        print
        print "Random numbers produced: ",

    for i in range(len(criterion)):
        if criterion[i]:
            sinusoid.append(first[i])
            if len(sinusoid) >= num:
                print "done"

                return sinusoid
        if verb:
            display_progress(len(sinusoid),num)

    return False
