from numpy import *
import random
thetas = []
X = []
y = []
trainFile = open("train.csv", 'r')
testFile = open("test.csv", 'r')
submitFile = open("NESubmit.csv", 'w')
trainLines = trainFile.readlines()
trainFile.close()
isFirst = True
i = 0
while i < 2:
    j = 0
    theta = []
    while j < 385:
        theta.append(random.uniform(-1e-4,1e-4))
        j+=1
    thetas.append(theta)
    i+=1
print thetas
i = -1
for l in trainLines :
    if isFirst :
        isFirst = False
        continue
    i+=1
    l = l.strip('\n')
    xx = []
    tokens = l.split(',')
    print tokens[1]
    y.append(float(tokens[1]))
    ii = 1
    while True:
        xx.append(float(tokens[ii+1]))
        ii+=1
        if ii >= 385:
            break
    X.append(xx)

