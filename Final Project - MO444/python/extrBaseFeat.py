"""
	Extracts Statistical Features

	This method extracts features based on statistical
	information of each image within the 
	directory pointed by argv[1]. Then, it writes
	down the features into a CSV-like file pointed by argv[2]
	These features are considered the baseline in our
	work

	Authors: Felipe Belem and Sarah Almeida
"""

# Packages
from skimage.io import imread
import sys, glob, os, math
import numpy as np

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
fp = open(sys.argv[2], "w")

# Change to the directory given
os.chdir(sys.argv[1])

# For every file within the directory
for file in sorted(glob.glob("*.pgm")):
	img = imread(file)

	# Extract features
	meanVal = np.mean(img[:])
	maxVal =  np.max(img[:])
	stdVal = np.std(img[:])
	varVal = np.var(img[:])
	entrVal = H(img)

	# Write in file
	fp.write(file + "," + str(meanVal) + "," + str(maxVal) + "," + str(stdVal) + "," \
		+ str(varVal) + "," + str(entrVal) + "\n")

# Close file
fp.close()
