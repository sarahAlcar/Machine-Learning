"""
	Random Forest Regressor

	This method uses the random forest regressor (RF)
	to try predicting the values of a given image 
	(pointed by argv[4]), after training the model considering
	the train set (pointed by argv[1]), and its labels (pointed
	by argv[2]). argv[3] denotes which label to analyze

	Authors: Felipe Belem and Sarah Almeida
"""

# Packages
from skimage.io import imread
from sklearn.ensemble import RandomForestRegressor
from skimage.feature import greycomatrix, greycoprops
from sklearn.model_selection import train_test_split

import sys, glob, os
import numpy as np

# Reads the samples and the labels
x = np.loadtxt(sys.argv[1], delimiter=',')
y = np.loadtxt(sys.argv[2], delimiter=',')

# Remove the IDs column
no_id_x = x[:,1:]
no_id_y = y[:,int(sys.argv[3])]

# Instantiate the RF with default params
rndfor = RandomForestRegressor(n_jobs=-1)

# Split data into test and train
x_train, x_test, y_train, y_test = train_test_split(no_id_x, no_id_y, test_size=0.33)

# Train model
rndfor.fit(x_train, y_train)

# Read input image
img = imread(sys.argv[4])

glcm = greycomatrix(img, distances=[1], angles=[0, np.pi/6, np.pi/4, np.pi/3, np.pi/2], levels=256, normed=True)

# Extract features
contrast = greycoprops(glcm, prop="contrast")
diss = greycoprops(glcm, prop="dissimilarity")
homo = greycoprops(glcm, prop="homogeneity")
energy = greycoprops(glcm, prop="energy")
corr = greycoprops(glcm, prop="correlation")
asm = greycoprops(glcm, prop="ASM")

# Compose feature vector
img_feat = np.zeros(shape=(1,contrast.shape[1]*6))

for i in range(contrast.shape[0]):
		for j in range(contrast.shape[1]):
			img_feat[i,j*6] = contrast[i,j]
			img_feat[i,j*6+1] = diss[i,j]
			img_feat[i,j*6+2] = homo[i,j]
			img_feat[i,j*6+3] = energy[i,j]
			img_feat[i, j*6+4] = corr[i,j]
			img_feat[i, j*6+5] = asm[i,j]

img_feat = np.reshape(img_feat, (1,-1))

# Predict values
pred = rndfor.predict(img_feat)

print pred[0]