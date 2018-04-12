import random 

x = []
y = []
somewhereobertherainbowwayuphigh = []
numPoints = 100

def makeRandomData():
	global x
	global y

	for i in range(numPoints):
		x.append(random.randint(-50,50))
		y.append(random.randint(-50,50))

def classifyData():
	for i in range(int((len(x) + len(y))/2)):
		aboveFunc = y[i] >= x[i]
		if aboveFunc:
			somewhereobertherainbowwayuphigh.append(1)
		else:
			somewhereobertherainbowwayuphigh.append(0)

def generateTrainingData():			
	makeRandomData()
	classifyData()	

def getTrainingData(index):
	return x[index], y[index]