"""
	Propagate values in group

	This method uses K-Means in order to group
	unlabeled samples by its features, considering
	a set of samples as seeds (which are labeled).
	Then, it propagates the seeds labels to every
	sample within each group. The features are read
	in a CSV file pointed by argv[1], while the seeds
	features are given by argv[2] (and its values by
	argv[3]). The final propagation results are written
	in an CSV-like file (pointed by argv[4])

	Authors: Felipe Belem and Sarah Almeida
"""

# Packages
from sklearn.cluster import KMeans
import sys, glob, os
import numpy as np

# Create output file
fp = open(sys.argv[4], "w")

# Dataset features
x = np.loadtxt(sys.argv[1], delimiter=',')

# Seeds features and labels
seeds_y = np.loadtxt(sys.argv[2], delimiter=',')
seeds_x = np.loadtxt(sys.argv[3], delimiter=',')

# Instantiate K-Means
kmeans = KMeans(n_clusters = seeds_x.shape[0], init=seeds_x[:,1:],max_iter=1)

# Predict the values
pred = kmeans.fit_predict(x[:,1:])

# Write in the output file
for i in range(x.shape[0]):
	label = pred[i]
	
	fp.write(str(int(x[i,0])))
	for j in range(1,y.shape[1]):
		fp.write("," + str(seed_y[label,j]))
	fp.write("\n")

fp.close()
