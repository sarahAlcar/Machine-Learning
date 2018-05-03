import numpy as np
from numpy import loadtxt, zeros, ones, array, linspace, logspace, mean, std
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
from sklearn.metrics import mean_absolute_error
from numpy.linalg import inv
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def compute_hypothesis (xFeatures, theta):
    hypothesis = xFeatures.dot(theta)
    return hypothesis
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def cost (xFeatures, yTarget, theta, mExamples, hypothesis):
   error = (hypothesis-yTarget)**2
   jCost = (1.0/(2 * mExamples))*error.sum()
   return jCost
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def gradient_descent (xFeatures, yTarget, theta, mExamples, alpha, maxIter, nFeatures, tolerance, lbd):
    jCost_history = zeros(shape=(maxIter, 1))
    
    for i in range(maxIter):
        hypothesis = compute_hypothesis (xFeatures, theta).flatten( )

        for j in range(nFeatures):
            x = xFeatures[:,j]
            error_x = (hypothesis - yTarget)*x
            theta[j][0] = theta[j][0] - alpha * (((1.0 /mExamples) * error_x.sum())+(lbd/mExamples+theta[j][0]))
    
        jCost_history[i, 0] = cost(xFeatures, yTarget, theta, mExamples, hypothesis)
        if (i > 0 and (abs(jCost_history[i, 0] - jCost_history[i-1, 0])<tolerance  or jCost_history[i-1, 0] < jCost_history[i, 0])):
            break
    return theta, jCost_history
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def run_tests (test, test_target, theta):
    print "*********Calculating final hypothesis*********"
    results = test.dot(theta)
    print "*********Calculating difference*********"
    diff = test_target - results
    erro = mean(abs(diff))
    print "Erro mean : ",erro
    return diff
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def feature_normalization(x,n):
    mean_r = []
    std_r = []

    x_norm = x

    for i in range(n):
        m = mean(x[:, i])
        s = std(x[:, i])
        mean_r.append(m)
        std_r.append(s)
        x_norm[:, i] = (x_norm[:, i] - m) / s

    return x_norm
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def poly (xFeatures):
    a = xFeatures
    a[:, 1] =  xFeatures[:, 1] ** 5
    a[:, 9] =  xFeatures[:, 9] ** 10
    a[:, 12] =  xFeatures[:, 12] ** 15
    a[:, 14] =  xFeatures[:, 14] ** 5
    return a
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
def NormEq (xFeatures, yTarget):
   theta = np.linalg.inv(xFeatures.T.dot(xFeatures)).dot(xFeatures.T).dot(yTarget)
   print "NORMAL EQ"
   return theta
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------Train Main Section -------------------------------------------------------------------

#Load the dataset
dataTrain = loadtxt('train-20coded.txt', delimiter=',')
dataTest = loadtxt('test-20coded.txt', delimiter=',')
dataTarget = loadtxt('test_target.txt', delimiter=',')


mExamples = dataTrain.shape[0]# Number of Examples in train
nFeatures = dataTrain.shape[1]# Number of Feature in train

xF = dataTrain[:, 0:nFeatures-1]# Segregating features from target
xPoly = poly(xF) #polinomial operations on features
xTrainNormalized = feature_normalization (xPoly, nFeatures-1)# Normalizing features
yTarget = dataTrain[:,nFeatures-1]# Defining target


xFeaturesBias = ones(shape=(mExamples,nFeatures))# Creates bias matrix to merge with X
xFeaturesBias[:, 1:nFeatures] = xTrainNormalized # Add a column of ones to X (interception data)

#theta = zeros(shape=(nFeatures, 1))
#theta = ones(shape=(nFeatures, 1))#Initialize theta parameters with 1
theta = np.random.rand (nFeatures, 1)#Initialize theta parameters with random values


maxIter = 5000 # maximum number of iterations 
alpha = 0.0005  # alpha value for GD
lbd = -100000
tolerance = 0.0001 # tolerance for GD

theta, J_history = gradient_descent(xFeaturesBias, yTarget, theta, mExamples, alpha, maxIter, nFeatures, tolerance, lbd)
print "*********End of trainning*********"
print "*********J HISTORY*********"
print J_history # GD cost history
print "*********end HISTORY*********"

#-----------------------------------------------Test Main Section-------------------------------------------------------------------

mExamples_test = dataTest.shape[0]# Number of Examples in train
nFeatures_test = dataTest.shape[1]# Number of Feature in test (must be the same as nFeatures)

test = dataTest.reshape(mExamples_test, nFeatures_test)
testPoly = poly(test)#polinomial operations on features
xTestNormalized = feature_normalization (testPoly, nFeatures-1)# Normalizing features
print "*********Test loaded*********"

testBias = ones(shape=(mExamples_test,nFeatures_test+1))# Creates bias matrix to merge with test
testBias[:, 1:nFeatures] = xTestNormalized # Add a column of ones to test (interception data)
print "*********Test with bias*********"

test_target = dataTarget # Loads target data for test
print "*********Target loaded*********"

diverge = run_tests (testBias, test_target, theta)# final error result
#normtt = NormEq (xFeaturesBias, yTarget)
#normi = run_tests (testBias, test_target, normtt)# final error result

