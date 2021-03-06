import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math
import numpy.random as rand
import scipy.optimize as opt
from MyGaussianPDFFinal import *



#exponential pdf which extends the PDF class
class ExponentialPDF(PDF):

    def __init__(self,a,b,tau):
        PDF.__init__(self,a,b)
        self.tau=tau
        self.maxVal=self.maxValue(a,b,stepSize)

	#exponential decay function
    def evaluate(self, x):
	    coef=self.tau**-1
	    expon=-x*(self.tau**-1)
            return coef*math.exp(expon)

	#generates a new random number from a exponential distribution
    def next(self):
        fromExponential=False
        while fromExponential==False:
            x1=rand.random()
            x1=self.toRangeAB(self.a,self.b,x1)
            y1=self.evaluate(x1)
            y2=self.toRangeFmax(self.maxVal, rand.random())
            if y2<y1:
                fromExponential=True
                return x1
            else:
                pass


stepSize = 0.0001

#exponential decay function where tau is an input
def fitFunc(x,t):
    return (1/t)*np.exp(-x/t)

#negative log likelihood 
def nll(vals,tau):
    return -sum([np.log2(fitFunc(vals[x],tau)) for x in range(0,len(vals))])

#minimises by comparing negative log likelihoods of two values of tau
def minimize(vals):

    stepSize = 0.01
    improvement = True
    initialTau = 2.0
    tau=initialTau
    currentNLL = nll(vals,tau)
#    iterations=0
#    print "here"
#    a,b =opt.curve_fit(fitFunc,vals,[fitFunc(vals[x],initialTau) for x in range(0,len(vals))])
#    return a
    while improvement:
        nextNLL = nll(vals, tau+stepSize)
        if nextNLL < currentNLL:
            tau=tau+stepSize
            currentNLL=nextNLL
        else:
            improvement=False
    return tau

## My Attempt at improving the minmiser
'''        if math.fabs(nextNLL - currentNLL) >2:
#            print "here"
            stepSize *=1.2
            tau = tau+stepSize
            currentNLL = nextNLL
#            iterations+=1
        elif math.fabs(nextNLL - currentNLL) >0.1:
#            print "here2"
            stepSize = 0.01
            tau = tau+stepSize
            currentNLL = nextNLL
#            iterations+=1
        elif math.fabs(nextNLL - currentNLL) >0.00001 and iterations <=1000:
#            print "here3"
            stepSize*=0.5
            tau = tau+stepSize
            currentNLL = nextNLL
            iterations+=1'''


#generate decay times and return tau estimate				
def runI():
	#defines range
    a = 0
    b = 15
   
    tau=2.2
    targetValue=1000 #ammount of random numbers generated+


    expo=ExponentialPDF(a,b,tau)

	#list of points from the exponential distribution
    values=[0 for x in range(0,targetValue)] 
    for i in range(0,targetValue):
        values[i]=expo.next()


	#Maximum Likelihood estimation of tau by taking derivative of log likelihood, setting it to 0 and solving for tau	
#    MLEst = (sum(values))/targetValue 

    tauPredicted = minimize(values)
    return tauPredicted

#run program 5000 times and print expected tau values to a file	
def main():
	f = open("decayTimes.txt","w")
	tau = [0 for x in xrange(0,5000)]
	for i in range(0,len(tau)):
		tau[i]=runI()
        	f.write(str(tau[i]) + '\n')
	print tau
	plt.hist(tau, bins=15)
	plt.show()
	f.close()



if __name__=='__main__':
    main()

