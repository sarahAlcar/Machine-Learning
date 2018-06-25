"""
	Linear Regression Algorithm

	This method uses the linear regression algorithm
	to try predicting the values of a given image 
	(pointed by argv[4]), after training the model considering
	the train set (pointed by argv[1]), and its labels (pointed
	by argv[2]). argv[3] denotes which label to analyze

	Authors: Felipe Belem and Sarah Almeida
"""

"""
	Calculates the entropy of a given image

	:param data - Input image

	:return Shannon entropy of the input image
"""
def H(data):
	entropy = 0.0
	maxColor =  np.max(img[:])

	for x in range(maxColor):
		unique, counts = np.unique(x, return_counts=True)
		p_x = counts/float(data.size)

		if p_x > 0:
			entropy += - p_x*math.log(p_x, 2)

	return entropy[0]

# Create the output file
from skimage.io import imread
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import sys, glob, os, math
import numpy as np

# Reads the samples and the labels
x = np.loadtxt(sys.argv[1], delimiter=',')
y = np.loadtxt(sys.argv[2], delimiter=',')

# Remove the IDs column
no_id_x = x[:,1:]
no_id_y = y[:,int(sys.argv[3])]

# Instantiate the linear regression with default params
linReg = LinearRegression(fit_intercept=True, normalize=True, n_jobs=-1)

# Split data into test and train
x_train, x_test, y_train, y_test = train_test_split(no_id_x, no_id_y, test_size=0.33)

# Train model
linReg.fit(x_train, y_train)

# Read input image
img = imread(sys.argv[4])

# Extract features
meanVal = np.mean(img[:])
maxVal =  np.max(img[:])
stdVal = np.std(img[:])
varVal = np.var(img[:])
entrVal = H(img)

# Compose feature vector
img_feat = np.zeros(5)
img_feat[0] = meanVal
img_feat[1] = maxVal
img_feat[2] = stdVal
img_feat[3] = varVal
img_feat[4] = entrVal

img_feat = np.reshape(img_feat, (1,-1))
# Predict values
pred = linReg.predict(img_feat)

print pred[0]
