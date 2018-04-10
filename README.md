# APCSP
this repo is for our APCSP Preformance task

<h1>Task:</h1>
<br>
Our Task is to make a program that can recive a mathmatical function then make training data based on random points that have been determend to be above or below the graph of the function. Then based on that training data, train a neural network to guess wether a point is above or bellow the graph.  
<h1>Algorithm:</h1>
<br>
1. initilize the network with random weights to start with
<br>2. Pass each points cordinance through the neural network. If the the network is right add one to a score varible. If it is wrong, take one point from the score. Repeat for each point in the training data.   
<br>3. Increment the first weight or weight(N) by .01 and run through all of the training data again; record the score. Then decrement the first weight by .02(This is to counteract the first increment to the weight, this overall results in a change of -.01 in the weight), then run through all the training data again after the decrement; record the score.
<br>4. Based on the preformance of the network with the incremented or decremented weight, perminatly set the weight to the value of the best preforming network. If both networks preformed worst then the original, keep the weight the same and make no change. 
<br>5. Move to the next weight in the network and repeat Step 2. Until you get to the last weight. 
<br>6. Repeat Step 1.  
