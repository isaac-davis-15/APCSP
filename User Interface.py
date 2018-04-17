import training
import main
import learning
import network
import os
import time

numPoints = int(input("Num of points? "))
function = input("Function of graph? Y= ")
rangeX = int(input("What is the range of the graph on the X-axis? "))
rangeY = int(input("What is the range of the graph on the Y-axis? "))

def displayData (weights,score)
	print("This is the curent set of the weights the program is running through." + str(weights))
	print("This is the current score of our point classifyer. In just a few minutes you will have your answer:" + str(score))
	print("This is the current closest the program has come to finding your function on the x-axis: " + str(training.x))
	print("This is the current closest the program has come to finding your function on the y-axis: " + str(training.y))
	print("The scores and sets will update every .5 seconds")
        time.sleep(.5)
	os.system("cls")
