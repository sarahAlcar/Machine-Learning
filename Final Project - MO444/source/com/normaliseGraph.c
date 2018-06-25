/*
Copyright ESIEE (2009) 

m.couprie@esiee.fr

This software is an image processing library whose purpose is to be
used primarily for research and teaching.

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software. You can  use, 
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info". 

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability. 

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or 
data to be ensured and,  more generally, to use and operate it in the 
same conditions as regards security. 

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.
*/

/* authors : J. Cousty - L. Najman and M. Couprie */

#include <stdio.h>
#include <stdint.h>
#include <sys/types.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#include <mccodimage.h>
#include <mcimage.h>
#include <mcweightgraph.h>

void usage(char *arg){
  printf("#################################################################\n\n");
  printf("USAGE: %s IN.pgm OUT.graph [mode [lambda t] ]\n", arg); 	
  printf("\t The optional parameter mode allows one to specify\n");
  printf("\t a transform applied to edges weights before normalisation\n");
  printf("\t If mode = 0, then square root is applied.\n");
  printf("\t If mode = 1, then log_2 is applied\n");
  printf("\t If mode = 2, then a sigmoid function is applied :\n");
  printf("\t \t f(x) = 1 / (1 +exp(-lambda.(x + t)))\n");
  printf("\t If mode = 3 , then a scale is applied\n");
  printf("#################################################################\n\n");
}

int32_t max(int32_t a, int32_t b){
  if (a<b) return b;
  else return a;
}

/***********************************************************/
/* Input:                                                  */

/* Output:                                                 */

/*                                                         */

/***********************************************************/


int32_t main(argc, argv) 
     /* =============================================================== */
     int32_t argc; char **argv; 
{
  graphe *g;
  int32_t u, nE, mode,value;
  double aux;
  double *Fv, tmp, Max,Min; 
  double t, lambda;
  
  mode = -1;
  if( (argc != 3) && (argc != 4) && (argc != 6)){
    usage(argv[0]);
    exit(1);
  }
  
  g = ReadGraphe(argv[1], &Fv);
  nE = g->ind;

  if(argc == 4) mode = atoi(argv[3]);

  if(argc == 6){
    mode = atoi(argv[3]);
    lambda = atof(argv[4]);
    t = atof(argv[5]);
  }

  switch(mode){
  case 0: // Square Root
    for(u = 0; u < nE; u++) {
      aux = sqrt(getweight(g,u));
      value = (uint32_t)aux;

      if( value > 255 ) { value = 255;}
      else if( value < 0 ) { value = 0; }

      setweight(g, u, value);

    }
    break;
  case 1: // Logarithm
    for(u = 0; u < nE; u++) {
      aux = log(getweight(g,u))/log(2);
      value = (uint32_t)aux;

      if( value > 255 ) { value = 255;}
      else if( value < 0 ) { value = 0; }
      setweight(g, u, value);
    }
    break;
  case 2: // Sigmoid function
    Max = 0;
    for(u = 0; u < nE; u++) {
      if(getweight(g, u) > Max) { Max = getweight(g, u); }
    }
    
    for(u = 0; u < nE; u++) {
      setweight(g, u, getweight(g,u)/Max);
    }
    for(u = 0; u < nE; u++) {
      if(getweight(g,u) > 0.0) {
       setweight(g, u, 1 / (1 + exp(-lambda * (getweight(g,u) + t) )));
      }
    }
    
    for( u = 0; u < nE; u++ ) {
      if( getweight(g,u) > 0.0 ) {
        setweight( g, u, (uint32_t)( 255 * getweight(g,u) ) );
      }
      else {
        setweight( g, u, 0 );
      }
    }

    break;
  case 3: // Scale function
    Max = Min = getweight( g, 0 );
    for(u = 0; u < nE; u++) {
      if(getweight(g, u) > Max) { Max = getweight(g, u); }
      else if(getweight(g, u) < Min) { Min = getweight(g, u); }
    }

    for(u = 0; u < nE; u++) {
      aux = ( ( getweight(g,u) - Min ) * 255.0 ) / (float)( Max - Min ); 
      value = (uint32_t)aux;

      setweight(g, u, value);
    }
    break;
  }


  SaveGraphe(g, argv[2], Fv);
  terminegraphe(g);
  free(Fv);

  return 0;
}
