import network
import training

weights = network.weights
score = 0

def incrementWeight(index, inputScore):
	weights[index] += 10

def decrementWeight(index, inputScore):
	weights[index] -= 10
	
def scoreNetwork():
	global score
	score = 0
	
	for i in range(training.numPoints):
		if network.think(i) >= 0.5 and training.pointClass[i]:
			score += 100
	return (score/training.numPoints)
	
def trainNetwork():
	score = 0 
	newWeights = 0
	for i in range(training.numPoints):
		if network.think(i) >= 0.5 and training.pointClass[i]:
			score += 1
		elif network.think(i) < 0.5 and not training.pointClass[i]:
			score += 1
	while newWeights < score
	network.setupWeights(network.numOfWeights)