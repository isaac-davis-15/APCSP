import network
import training
import learning
import interface
import time
import os

#Set up the Neural Network and Generate Training Data
network.createNetwork()
training.generateTrainingData()
score = 0
iderations = 0
while 1==1:
	for i in range(training.numPoints):
		if network.think(i) >= 0.5 and training.pointClass[i]:
			score += 1
		elif network.think(i) < 0.5 and not training.pointClass[i]:
			score += 1
		iderations += 1
		
	interface.displayData(network.weights, (score/iderations))
	learning.trainNetwork()
	os.system("cls")