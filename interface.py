import training
import learning
import network
import os
import time

# numPoints = int(input("Num of points? "))
# function = input("Function of graph? Y= ")
# rangeX = int(input("What is the range of the graph on the X-axis? "))
# rangeY = int(input("What is the range of the graph on the Y-axis? "))

def displayData(weights, score):
	print("This is the current set of the weights the program is running through." + str(weights))
	print("This is the current score of our point classifier. In just a few minutes you will have your answer:" + str(score))
	print("The scores and sets will update every .5 seconds")
	time.sleep(.5)
	
	
def displayDat(weights, score):
	print("------------------------------------------------")
	print("| Neural Network classifying points on a graph |")
	print("------------------------------------------------")
	print("Score: %" + str(score*100))
	print("Weights: " + str(weights))
	print("Hidden Layer Activations: " + str(network.hiddenLayerOuptput))