# GENERATING THE DATA FOR CSV FILE
import numpy as np
from random import random
import csv



# Generates a list containing n-number of factors
def populate_factors(n):
	s = 'Factor '
	f = [s+str(i) for i in range(1,n+1)]
	return f

# Randomly generates a list of sigma values (std deviations) corresponding to the number of factors between [0.1,0.3] 
def get_std_devs(factors):
	std_devs = []
	for i in factors:
		v = np.random.normal(0,.05,1) + np.random.uniform(0.1,0.25,1)
		std_devs.append(v)
		# v = random()

		# scaled_value = 0.1 + (v * (0.3 - 0.1))
		# std_devs.append(scaled_value)
	return std_devs


# Samples from a normal distribution n-times to get the pct change for n-number of data points using the sigma values generated
def get_pct_changes(n,std_devs):
	p = []
	for i in std_devs:
		s = np.random.normal(0,i,n)
		p.append(s)
	return p

def write_csv():
	myData = [factors,pct_changes]
	myFile = open('testingScript.csv', 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData)





numFactors=100
numDataPoints = 100


factors = populate_factors(numFactors)
std_devs = get_std_devs(factors)
pct_changes = get_pct_changes(numDataPoints,std_devs)
write_csv()
# weights = []
# returns = []

# write





