#!/bin/sh
linux/bin/ppm2graph $1 1 tmp/_1.graph

linux/bin/normaliseGraph tmp/_1.graph tmp/_1norm.graph 2 18 -0.3

linux/bin/extinctionvalues tmp/_1norm.graph 5 tmp/_2.graph tmp/BM.txt
linux/bin/uprooting tmp/_2.graph tmp/_3.graph
linux/bin/ultramopen tmp/_3.graph tmp/_4.graph tmp/BM.txt

linux/bin/normaliseGraph tmp/_4.graph tmp/_5.graph 2 18 -0.3

linux/bin/graph2pgm tmp/_5.graph 0 tmp/_6.pgm
linux/bin/float2byte tmp/_6.pgm 0 $2 

linux/bin/graph2pgm tmp/_1norm.graph 0 tmp/_1grad.pgm
linux/bin/float2byte tmp/_1grad.pgm 0 $2_grad.pgm

 rm -r tmp/_* tmp/BM.txt