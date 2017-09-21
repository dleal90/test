import matplotlib.pyplot as mp


#
# Draws the actual plot and exports it as a png.
#
def DrawPlot(ys, title="", verbose=True, filename="graph"):

    if (verbose):
        print("Generating Plot...")

    # Plot title
    titleYpos = max(ys)
    titleXpos = int((len(ys)-1)/2)
    mp.text(titleXpos, titleYpos, title)

    # Make plot
    mp.plot(ys)

    # Save plot
    mp.savefig("Output/{}.png".format(filename), bbox_inches="tight") 

    if (verbose):
        print("Done!")
