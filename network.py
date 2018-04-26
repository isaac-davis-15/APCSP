#=======================================================================================================
#Isaac Davis 4/10/18
#
#This script contains functions that can be used by other Python scripts.
#The functions calculate all of the math and algorithms for the neural network to function.  
#This script is specifically for a network with 2 inputs 1 hidden layer with 3 neuron and 1 output. 
#
import random as r
import math
import training
#=======================================================================================================

weights = []
numNuronsInLayer = [2, 3, 1]
numOfLayers = len(numNuronsInLayer)
numOfWeights = 0
hiddenLayerOuptput = []

def setupWeights(num):
	global weights
	
	weights = []
	for i in range(num):
		randomWeight = r.uniform(-5, 5)
		weights.append(round(r.uniform(-5, 5), 3))
	
def initNetwork():
	global numOfWeights
	
	numOfWeights = 0
	numNuronsInLayer.append(0)
	for i in range(len(numNuronsInLayer) - 1):
		numOfWeights += numNuronsInLayer[i] * numNuronsInLayer[i+1]
	
	setupWeights(numOfWeights)

def createNetwork():
	initNetwork()

def sigmoid(x):
	try:
		if x >= 50:
			return 1
		elif x <= -50:
			return 0
		else:
			return 1/(1 + math.exp(-x))
	except OverflowError:
		print("Give up on your programing Carear")
		exit()
	
def neuron(inputArr, weightArr):	
	sum = 0
	for i in range(int((len(inputArr) + len(weightArr))/2)):
		cal = inputArr[i] * weightArr[i]
		sum += cal	
	return sigmoid(sum)
	
def think(index):
	global numNuronsInLayer
	global weights 
	global hiddenLayerOuptput
	x, y = training.getTrainingData(index)
	
	#setting up the hiddenLayer
	hiddenLayerInput = [x, y]
	hiddenLayerOuptput = []
	hiddenLayerWeights = []
	for i in range(6):
		hiddenLayerWeights.append(weights[i])
	#hidden Layer calculation
	for i in range(0, 3):
		inputedWeights = []
		inputedWeights.append(hiddenLayerWeights[i])
		inputedWeights.append(hiddenLayerWeights[i+3])
		
		neuronOutput = neuron(hiddenLayerInput, inputedWeights)
		hiddenLayerOuptput.append(round(neuronOutput, 2))
	
	return neuron(hiddenLayerOuptput, weights[6:8])

def thinkPoints(x, y):
	global numNuronsInLayer
	global weights 
	global hiddenLayerOuptput
	
	#setting up the hiddenLayer
	hiddenLayerInput = [x, y]
	hiddenLayerOuptput = []
	hiddenLayerWeights = []
	for i in range(6):
		hiddenLayerWeights.append(weights[i])
	#hidden Layer calculation
	for i in range(0, 3):
		inputedWeights = []
		inputedWeights.append(hiddenLayerWeights[i])
		inputedWeights.append(hiddenLayerWeights[i+3])
		
		neuronOutput = neuron(hiddenLayerInput, inputedWeights)
		hiddenLayerOuptput.append(round(neuronOutput, 2))
	
	return neuron(hiddenLayerOuptput, weights[6:8])	