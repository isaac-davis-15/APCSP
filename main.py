import network
import training

#Set up the Neural Network and Generate Training Data
network.createNetwork()
training.generateTrainingData()

#Run the Network through all the training data
#And get an initial score
for i in range(training.numPoints):
	above = "Negative"
	
	x, y = training.getTrainingData(i)
	
	if network.think(x, y) >= 0.5:
		above = "Positive"

	print("(" + str(training.x[i]) + ", " + str(training.y[i])+") " + str(training.somewhereobertherainbowwayuphigh[i]) + " | " + above)
	
