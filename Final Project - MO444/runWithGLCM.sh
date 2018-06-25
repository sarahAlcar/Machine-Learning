#!/bin/sh
linux/bin/ppm2graph $1 1 tmp/_1.graph

linux/bin/graph2pgm tmp/_1.graph 0 tmp/_1grad.pgm
linux/bin/float2byte tmp/_1grad.pgm 0 tmp/_nosigm_grad.pgm

SIGM_STEEP_GRAD_VAL="$(python python/glcm.py train_data/glcmGradFeats.csv train_data/glcmPropVals.csv 1 tmp/_nosigm_grad.pgm)"
SIGM_x0_GRAD_VAL="$(python python/glcm.py train_data/glcmGradFeats.csv train_data/glcmPropVals.csv 2 tmp/_nosigm_grad.pgm)"
SIGM_STEEP_SAL_VAL="$(python python/glcm.py train_data/glcmGradFeats.csv train_data/glcmPropVals.csv 3 tmp/_nosigm_grad.pgm)"
SIGM_x0_SAL_VAL="$(python python/glcm.py train_data/glcmGradFeats.csv train_data/glcmPropVals.csv 4 tmp/_nosigm_grad.pgm)"

linux/bin/normaliseGraph tmp/_1.graph tmp/_1norm.graph 2 $SIGM_STEEP_GRAD_VAL -"$SIGM_x0_GRAD_VAL"

linux/bin/extinctionvalues tmp/_1norm.graph 5 tmp/_2.graph tmp/BM.txt
linux/bin/uprooting tmp/_2.graph tmp/_3.graph
linux/bin/ultramopen tmp/_3.graph tmp/_4.graph tmp/BM.txt

linux/bin/normaliseGraph tmp/_4.graph tmp/_5.graph 2 $SIGM_STEEP_SAL_VAL -"$SIGM_x0_SAL_VAL"

linux/bin/graph2pgm tmp/_5.graph 0 tmp/_6.pgm
linux/bin/float2byte tmp/_6.pgm 0 $2 

linux/bin/graph2pgm tmp/_1norm.graph 0 tmp/_1grad.pgm
linux/bin/float2byte tmp/_1grad.pgm 0 $2_grad.pgm

 rm -r tmp/_* tmp/BM.txt