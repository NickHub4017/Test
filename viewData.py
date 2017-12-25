"""Example program to show how to read a multi-channel time series from LSL."""
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def collectData():
    dataSet=[]
    for i in range(0,250):
        sample, timestamp = inlet.pull_sample()
        #print(sample)
        dataSet.append(sample[:4])
    return dataSet


def animate(i):
    #pullData = collectData()
    dataArray =  collectData()
    xar = []
    yar = []
    i=0
    for eachLine in dataArray:
        if True:
            #x,y = eachLine.split(',')
            xar.append(i)
            yar.append(eachLine)
            i=i+1
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()


def getPeakIndataSet(dataSet):
    al=[]
    al.append(np.mean(dataSet, axis=0))
    return al


ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()

