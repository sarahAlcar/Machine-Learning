"""
	Extracts Grey Level Co-Occurrence Matrix Features

	This method extracts features based on the gray-level
	co-ocurrence matrix obtained by each image within the 
	directory pointed by argv[1]. Then, it writes
	down the features into a CSV-like file pointed by argv[2]

	Authors: Felipe Belem and Sarah Almeida
"""

# Packages
from skimage.io import imread
from skimage.feature import greycomatrix, greycoprops
import sys, glob, os, math
import numpy as np

# Create the output file
fp = open(sys.argv[2], "w")

# Change to the directory given
os.chdir(sys.argv[1])

# For every file within the directory
for file in sorted(glob.glob("*.pgm")):
	img = imread(file)

	glcm = greycomatrix(img, distances=[1], angles=[0, np.pi/6, np.pi/4, np.pi/3, np.pi/2], levels=256, normed=True)

	# Extract features
	contrast = greycoprops(glcm, prop="contrast")
	diss = greycoprops(glcm, prop="dissimilarity")
	homo = greycoprops(glcm, prop="homogeneity")
	energy = greycoprops(glcm, prop="energy")
	corr = greycoprops(glcm, prop="correlation")
	asm = greycoprops(glcm, prop="ASM")

	# Write in file
	fp.write(file)
	for i in range(contrast.shape[0]):
		for j in range(contrast.shape[1]):
			fp.write("," + str(contrast[i,j])+ "," + str(diss[i,j]) + "," + str(homo[i,j]) + "," + str(energy[i,j]) + "," + str(corr[i,j]) + "," + str(asm[i,j]))
	fp.write("\n")	

# Close file
fp.close()
