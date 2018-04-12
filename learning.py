import network
import training

weights = network.weights
score = 0

def incrementWeight(index, inputScore):
	weight[index] += (100 - inputScore) / 10	

def decrementWeight(index, inputScore):
	weight[index] -= (100 - inputScore) / 10
	
def scoreNetwork():
	global score
	score = 0
	
	for i in range(training.numPoints):
		x, y = training.getTrainingData(i)
	
		if network.think(x, y) >= 0.5 and training.pointClass[i]:
			score += 100
	return (score/training.numPoints)
	
def trainNetwork():
	beforeScore = scoreNetwork()
	
	for i in range(len(weights)):
		incrementWeight()
		scoreNetwork()
		decrementWeight() 
		
		