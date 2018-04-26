import network
import training
import learning
import interface
import time
import os
import atexit

#Set up the Neural Network and Generate Training Data
network.createNetwork()
training.generateTrainingData()
score = 0
iderations = 0
trainStage = True

def testNetwork():
	os.system("cls")

	while trainStage:
		print("Test the Network!!!")
		print("-------------------")
		interface.bestWeights = network.weights
		
		xInput = int(input("Give X point: "))
		yInput = int(input("Give Y point: "))
		
		if network.thinkPoints(xInput, yInput) >= 0.5:
			print("Above")
		else:
			print("Below")
			
atexit.register(testNetwork)
			
while trainStage:
	for i in range(training.numPoints):
		if network.think(i) >= 0.5 and training.pointClass[i]:
			score += 1
		elif network.think(i) < 0.5 and not training.pointClass[i]:
			score += 1
		iderations += 1
		
	interface.updateBest((score/iderations))
	learning.trainNetwork()
