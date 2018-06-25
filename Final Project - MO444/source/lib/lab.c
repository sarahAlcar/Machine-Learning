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

/* authors : J. Cousty  */

#include <stdio.h>
#include <stdint.h>
#include <sys/types.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>

double decompand(double V){
  if (V <= 0.04045) return V/12.92;
  else return pow( (V+0.055) / 1.055, 2.4);		     
}

#define KAPPA 903.3
#define EPSILON  0.008856

double simplified(double v, double ref){
  double vv;
  vv = v / ref;

  if(vv > EPSILON) vv = pow(vv, 1.0/3.0);
  else vv = (KAPPA * vv + 16) / 116;

  return vv;
}

void lab(uint8_t R, uint8_t G, uint8_t B, double *l, double* a, double *b){
  double dr, dg, db, x, y, z;

  dr = decompand( ((double) R)/255 );
  dg = decompand( ((double) G)/255 );
  db = decompand( ((double) B)/255 );
  
  x = 0.4124564*dr +  0.3575761*dg  + 0.1804375*db;
  y = 0.2126729*dr +  0.7151522*dg  + 0.0721750*db;
  z = 0.0193339*dr +  0.1191920*dg  + 0.9503041*db;

  x = simplified(x, 0.95047);
  y = simplified(y, 1.0);
  z = simplified(z, 1.08883);

  (*l) = 116 * y - 16;
  (*a) = 500 * (x - y);
  (*b) = 200 * (y - z);
}

double labgrad(uint8_t Rx, uint8_t Gx, uint8_t Bx, uint8_t Ry, uint8_t Gy, uint8_t By){
  double lx, ax, bx, ly, ay, by;
  lab(Rx, Gx, Bx, &lx, &ax, &bx);
  lab(Ry, Gy, By, &ly, &ay, &by);
  
  return sqrt( (lx-ly) * (lx-ly) + (ax-ay) * (ax-ay) + (bx-by)*(bx-by) );   
}
