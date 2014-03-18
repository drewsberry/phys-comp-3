## My progress bar - maybe I'll need it later

even = np.zeros((num))

print "Random numbers produced: ",

for i in range(num):

    even[i] = rnd.uniform(0,2)

    percentage = 100*(i+1)/num

    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))

print
