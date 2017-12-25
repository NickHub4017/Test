"""Example program to show how to read a multi-channel time series from LSL."""
import numpy as np
import time
from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

def collectData():
    dataSet=[]
    for i in range(0,20):
        sample, timestamp = inlet.pull_sample()
        dataSet.append(sample[:4])
    return dataSet

def getPeakIndataSet(dataSet):
    return [np.mean(dataSet, axis=0),
    np.mean(dataSet, axis=1),
    np.mean(dataSet, axis=2),
    np.mean(dataSet, axis=3)]


while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    dataSet=collectData()
    peaks=getPeakIndataSet(dataSet)
    print peaks
    time.sleep(10)






