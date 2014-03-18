## Trying a numpy method, but I'll keep this in case the numpy one doesn't work out

def reject_accept(num):
    # Use reject-accept method to produce random numbers distributed as 
    # sin(theta) in 0 < theta < pi

    first = []
    second = []
    sinusoid = []

    print "Random numbers produced: ",

    for i in range(num):
        first.append(rnd.uniform(0,math.pi))
        second.append(rnd.uniform(0,1))

        if second[i] < math.sin(first[i]):
            sinusoid.append(first[i])

        display_progress(i+1,num)

    print
    print "Sinusoidal random number distribution using reject-accept method produced."

    return sinusoid
