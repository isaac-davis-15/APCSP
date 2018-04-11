#=======================================================================================================
#Isaac Davis 4/10/18
#
#This script contains functions that can be used by other Python scripts.
#The functions calculate all of the math and algorithms for the neural network to function.  
#This script is specifically for a network with 2 inputs 1 hidden layer with 3 neuron and 1 output. 
#
import random as r
#=======================================================================================================

weights = []
numNuronsInLayer = [2, 100, 1]
numOfLayers = len(numNuronsInLayer)
numOfWeights = 0

def setupWeights(num):
	global weights

	for i in range(num):
		weights.append(r.randint(-50, 50))
	
	print(weights)
	
def initNetwork():
	global numOfWeights
	
	numOfWeights = 0
	numNuronsInLayer.append(0)
	for i in range(len(numNuronsInLayer) - 1):
		numOfWeights += numNuronsInLayer[i] * numNuronsInLayer[i+1]
	print(numOfWeights)
	
	setupWeights(numOfWeights)

def createNetwork():
	initNetwork()

def think()