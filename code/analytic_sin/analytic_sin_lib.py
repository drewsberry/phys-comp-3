#External libraries
import numpy as np

def produce_randoms(num):
    # Produce num evenly distributed random numbers 

    print "Producing {} uniformly distributed random numbers... ".format(num)
    even = np.random.uniform(0,2,num)
    print "...done"

    return even

def trans_to_sin(even):
    # Translate evenly distributed random numbers to those distributed as 
    # sin(theta) in 0 < theta < pi, using analytic method

    num = len(even)

    print "Analytically transforming {} evenly distributed random numbers to "\
          "sinusoidally distributed ones...".format(num)
    sinusoid = np.arccos(1 - even)
    print "...done"

    return sinusoid
