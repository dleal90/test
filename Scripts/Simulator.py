import matplotlib.pyplot as mp
import random


#
# Draws the actual plot and exports it as a png.
#
def DrawPlot(ys, title="", ylab="", xlab="", verbose=True, filename="graph", useYbounds=True, ymin=0, ymax=100):

    if (verbose):
        print("Generating Plot...")

    # Set bounds
    if (useYbounds):
        padding = (ymax - ymin)*.1
        mp.ylim(ymin - padding, ymax + padding)
        
    # Make plot
    mp.title(title)
    mp.xlabel(xlab)
    mp.ylabel(ylab)
    mp.plot(ys)

    # Save plot
    mp.savefig("Output/{}.png".format(filename), bbox_inches="tight") 

    if (verbose):
        print("Done!")

#
# Simulates Present Values over time and returns the
# results as an array.
#
def GeneratePVs(coupon, years, noisefactor=.05):

    PV = []
    r = random.uniform(-.001, .005)

    previous = coupon
    for i in range(years):
        noise = random.uniform(1 - noisefactor, 1 + noisefactor)
        PV.append(previous/((1 + r)) * noise) # was (1+r**i) and "PV[i]" instead of "previous"
        previous = PV[i]

    print("r = {}".format(r))
    print("PV = {}".format(PV))

    return PV  

#
# Simulates a bond given a life-span and coupon amount.
#
def SimulateBond(coupon, life=10):
    PVs = GeneratePVs(coupon, life);
    DrawPlot(PVs, "Present Value", "US Dollars", "Years", filename="PVGraph")
    
