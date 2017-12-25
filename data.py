"""Example program to show how to read a multi-channel time series from LSL."""
import numpy as np
import time
from pylsl import StreamInlet, resolve_stream
from sklearn import svm

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0],max_buflen=1)

def collectData():
    dataSet=[]
    for i in range(0, 500):
        inlet.pull_sample()
    print(" Do for sampling:- ")
    a=time.time()
    for i in range(0,500):
        sample, timestamp = inlet.pull_sample()
        #print(sample)
        dataSet.append(sample[:4])
    print(time.time()-a)
    return dataSet

def getPeakIndataSet(dataSet):
    al=[]
    return np.mean(dataSet, axis=0).tolist()
    #return al

def getHandposition01Data():
    dataSet = collectData()
    return getPeakIndataSet(dataSet)

checkData01=[]
checkData02=[]
checkData03=[]
checkData04=[]
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    data=[]
    classes=[]

    for i in range(0,4):
        input("NEXT MOVE")
        print("Calibrating for "+str(i))
        for j in range(0,10):
            print("Press enter for get sample "+str(j)+" for calibrating " + str(i))
            temp=getHandposition01Data()
            data.append(temp)
            classes.append(i)
            if(i==0):
                checkData01=temp
            if(i==1):
                checkData02=temp
            if (i == 2):
                checkData03 = temp
            if (i == 3):
                checkData04 = temp
            time.sleep(2)

    #print(data)
    #print(classes)
    X=np.array(data)
    y=classes
    print("dataSet "+str(X))
    print("classes "+str(y))
    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X, y)
    print(clf.predict([checkData01]))
    print(clf.predict([checkData02]))
    print(clf.predict([checkData03]))
    print(clf.predict([checkData04]))

    input("Do 01")
    print(clf.predict([getHandposition01Data()]))
    input("Do 02")
    print(clf.predict([getHandposition01Data()]))
    input("Do 03")
    print(clf.predict([getHandposition01Data()]))
    input("Do 04")
    print(clf.predict([getHandposition01Data()]))
    time.sleep(10)






