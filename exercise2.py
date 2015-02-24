import numpy as np

"""Part A:

Unobserverd variables (Xt): Weather

Observed variables (Et): Umbrella

P(Xt | Xt-1) = 0.7
P(Et | Xt) = 0.9

Xt |  Xt-1 = no | Xt-1 = yes
no |     0.7    |    0.3 
yes|     0.3    |    0.7

Et | Xt = no | Xt = yes
no |   0.8   |   0.1
yes|   0.2   |   0.9

Assumptions:
1. The probability for rain does not change depending on whether it rained 3 days ago
2. The probabilities does not change over time."""

o = [np.matrix("0.1 0;0 0.8"), np.matrix("0.9 0;0 0.2")]#observational model
d = np.matrix("0.7 0.3;0.3 0.7") #dynamic model
startProb = np.matrix("0.5;0.5") #startsansynligheten for regn eller ikke er 50/50

#print o[0],'\n','\n', o[1]
def normalise(answer):
	return answer/sum(answer)

def forward(umbrella, f):
	return normalise( np.dot( np.dot( o[umbrella], np.transpose(d) ), f) )#equation 12

def Backward(umbrella, b):
	return np.dot(np.dot(d, o[umbrella]), b)#equation 13

# e = om paraply er true eller false
# prob_Of_Rain = sansynlighet for regn
def PartB(e):
	prob_Of_Rain = startProb
	for i in e: #itererer over alle dager en har informasjon om paraplyen.
		#print 'i', i
		prob_Of_Rain = forward(i, prob_Of_Rain) #update prob_of_rain basert paa eq. 12
	return np.transpose(prob_Of_Rain)

def forwardBackward(e):
	n = len(e) #antall dager med kunnskap om paraply
	prob_Of_Rain = range(n+1)#vektor med sans for rein for hver dag
	prob_Of_Rain[0] = startProb#starter med sans = 50/50
	sv = range(n)#vektor med smoothed sansynligheter for regn
	b = np.ones( (len(startProb), 1) )

	for i in xrange(1, n):#iterer forward
		prob_Of_Rain[i] = forward(e[i-1], prob_Of_Rain[i-1])

	for i in range(n-1, -1, -1):#iterer backward
		sv[i] = normalise( np.multiply( prob_Of_Rain[i+1], b ) )
		b = Backward(e[i], b)
	return sv[0]
 
print 'Part B:', PartB([1, 1, 0, 1, 1]), '\n'
print 'Part C:', forwardBackward([1, 1, 0, 1, 1])