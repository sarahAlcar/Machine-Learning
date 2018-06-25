"""
	Support Vector Regressor

	This method uses the support vector regressor (SVR)
	to try predicting the values of a CSV file (pointed
	by argv[1]), and measuring its error given its labels
	(pointed by argv[2]). argv[3] denotes which label to analyze.

	Authors: Felipe Belem and Sarah Almeida
"""

#Packages
from sklearn.svm import SVR
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

import sys, glob, os
import numpy as np

# Reads the samples and the labels
x = np.loadtxt(sys.argv[1], delimiter=',')
y = np.loadtxt(sys.argv[2], delimiter=',')

# Remove the IDs column
no_id_x = x[:,1:]
no_id_y = y[:,int(sys.argv[3])]

# Instantiate the SVR with default params
svr = SVR()

# Instantiate the K-Fold Cross Validation
kf = KFold(n_splits=10)
kf.get_n_splits(no_id_x)

# For every fold
fold = 0 
for train_index, test_index in kf.split(no_id_x):
	# Split train and test
	x_train, x_test = no_id_x[train_index], no_id_x[test_index]
	y_train, y_test = no_id_y[train_index], no_id_y[test_index]
	
	# Train model
	svr.fit(x_train, y_train)

	# Predict values
	pred = svr.predict(x_test)

	print pred

	# Estimate error
	mse = mean_squared_error(y_test, pred)

	# Print fold statistics
	fold = fold + 1
	print("Fold " + str(fold) + " : " + str(mse) )