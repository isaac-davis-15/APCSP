import training
import learning
import network
import os
import time

# numPoints = int(input("Num of points? "))
# function = input("Function of graph? Y= ")
# rangeX = int(input("What is the range of the graph on the X-axis? "))
# rangeY = int(input("What is the range of the graph on the Y-axis? ")) 

#Define some variables 
bestWeights = 0
bestScore = 0

def updateBest(score):
	global bestWeights
	global bestScore
	
	bestWeights = network.weights
	bestScore = score

def displayData(weights, score):
	print("This is the current set of the weights the program is running through." + str(weights))
	print("This is the current score of our point classifier. In just a few minutes you will have your answer:" + str(score))
	print("The scores and sets will update every .5 seconds")
	time.sleep(.5)
	
	
def displayDat():
	print("------------------------------------------------")
	print("| Neural Network classifying points on a graph |")
	print("------------------------------------------------")
	print("Best Score: %" + str(bestScore*100))
	print("Best Weights: " + str(bestWeights))
	  
def displayCurDat(weights, score):
	displayDat()
	print("")
	print("------------------------------------------------")
	print("")
	print("Current Score: " + str(score))
	print("Current Weights: " + str(weights))
	print("Best Hidden Layer Activations: " + str(network.hiddenLayerOuptput))