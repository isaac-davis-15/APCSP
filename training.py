import random 

x = []
y = []
pointClass = []
numPoints = 100 #interface.numPoints

def makeRandomData():
	global x
	global y

	for i in range(numPoints):
		x.append(random.randint(-50,50))#rangeX
		y.append(random.randint(-50,50))#rangeY

def classifyData():
	for i in range(int((len(x) + len(y))/2)):
		aboveFunc = y[i] >= x[i]
		if aboveFunc:
			pointClass.append(1)
		else:
			pointClass.append(0)

def generateTrainingData():			
	makeRandomData()
	classifyData()	

def getTrainingData(index):
	return x[index], y[index]
