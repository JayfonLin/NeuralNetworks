from numpy import *
from math import exp
import random
Theta1 = []
Theta2 = []
thetaVec = []
mylamda = 10
X = []
y = []
a = []
def init():
    
    j = 0
    tj = []
    while j < 384:
        k = 0
        tk = []
        while k < 385:
            tk.append(random.uniform(-1e-4,1e-4))
            k+=1
        tj.append(tk)
        j+=1
    Theta1 = tj
    
    print Theta1
    i = 0
    ti = []
    while i < 385:
        ti.append(random.uniform(-1e-4,1e-4))
        i+=1
    Theta2 = ti
    print Theta2
    print 'initialize end'

def readFile():
    trainFile = open("train.csv", 'r')
    testFile = open("test.csv", 'r')
    submitFile = open("NNSubmit.csv", 'w')
    trainLines = trainFile.readlines()
    trainFile.close()
    isFirst = True
    i = -1
    for l in trainLines :
        if isFirst :
            isFirst = False
            continue
        i+=1
        l = l.strip('\r\n')
        xx = []
        tokens = l.split(',')
        #print tokens[1]
        y.append(float(tokens[1]))
        ii = 1
        while True:
            xx.append(float(tokens[ii+1]))
            ii+=1
            if ii >= 385:
                break
        X.append(xx)
    X = mat(X)
    print 'read file end'

def g(pz):
    return 1.0/(1.0+exp(-pz))
def J():
    i = 0
    while i < 10000:
        
def h(x):
    i = 0
    while i < 384:
        j = 0
        zz = 0.0
        while j < 385:
            zz += (Theta1[i][j]*x[j]
            j+=1
        aa = g(zz)
        a.append(aa)
        i+=1
                   
if __name__ == "__main__":
    init()
    readFile()
    a.append(float(0.0))
    print "End"






