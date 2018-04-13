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
	print("Test")
	beforeScore = scoreNetwork()
	incrementScore = 0
	decrementScore = 0
	
	for i in range(len(weights)):
		#Add an to weight i and test the output
		#Then decrement the weight back to the original
		incrementWeight(i, beforeScore)
		incrementScore = scoreNetwork()
		decrementWeight(i, beforeScore)
		
		#Do the same as above but subtracting
		decrementWeight(i, beforeScore)
		decrementScore = scoreNetwork()
		incrementWeight(i, beforeScore)
		
		#compare if the network did better with
		#incremented weights or decremented weights
		if incrementScore > beforeScore:
			incrementWeight(i, beforeScore)
		elif decrementScore > beforeScore:
			decrementWeight(i, beforeScore)