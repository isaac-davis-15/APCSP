import random 

x = []
y = []

numPoints = 100

def makeRandomData():
	global x
	global y

	for i in range(numPoints):
		x.append(random.randint(-50,50))
		y.append(random.randint(-50,50))
    
makeRandomData()
print(x)
print(y)
