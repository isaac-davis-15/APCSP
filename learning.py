import network
import training
import interface
import time
import os

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
	newScore = 0
	trainIdderation = 0 
	for i in range(training.numPoints):
		if network.think(i) >= 0.5 and training.pointClass[i]:
			score += 1
		elif network.think(i) < 0.5 and not training.pointClass[i]:
			score += 1
	while newScore < score:
		newScore = 0
		network.setupWeights(network.numOfWeights)
		for i in range(training.numPoints):
			if network.think(i) >= 0.5 and training.pointClass[i]:
				newScore += 1
			elif network.think(i) < 0.5 and not training.pointClass[i]:
				newScore += 1
		if(trainIdderation % 15 == 0):
			os.system("cls")
			interface.displayCurDat(network.weights, (newScore/training.numPoints)*100)
			training.generateTrainingData()
		trainIdderation += 1	
	os.system("cls")

		