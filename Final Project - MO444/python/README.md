=============================================================
# Python modules
=============================================================
extrBaseFeat.py
	Extracts the statistical features for all images within a directory

extrGLCMFeat.py
	Extracts the texture features for all images within a directory	

glcm.py
	Predicts the optimal configuration values for a given gradient image, through a linear regression model, taking into account the texture features

linearRegr.py
	Predicts the optimal configuration values for a given gradient image, through a linear regression model, taking into account the statistical features

linearRegr_perf.py
	Evaluates the performance of the linear regression model by a K-Fold cross validation metod, and evaluated by the MSE

propVals.py
	Propagates the values of the seeds to all the cluster's samples, with respect to a given feature

rndforest.py
	Predicts the optimal configuration values for a given gradient image, through a Random Forest regression model, taking into account the texture features

rndforest_perf.py
	Evaluates the performance of the Random Forest regression model by a K-Fold cross validation metod, and evaluated by the MSE

svr.py
	Predicts the optimal configuration values for a given gradient image, through a Support Vector regression model, taking into account the texture features

svr_perf.py
Evaluates the performance of the Support Vector regression model by a K-Fold cross validation metod, and evaluated by the MSE
