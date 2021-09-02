#include <vector>
#include <cmath>
#include <boost/tuple/tuple.hpp>
#include "gnuplot-iostream.h"

const int DIM = 14;
const int LONGITUD = 1000000;


int graficar(float *red, int dim);
int imprimir(float *red, int dim);
int greaficar_vector(float *vector, int longitud);

int graficar(float *red, int dim){
    float frame[DIM][DIM];
    for (int n=0; n<dim; n++){
        for (int m=0; m<dim; m++){
            frame[n][m]=*(red +dim*n+m);
        }
    }

    Gnuplot gp;
    gp << "unset key\n";
    gp << "set pm3d\n";
    gp << "set hidden3d\n";
    gp << "set view map\n";
    gp << "set autoscale xfix\n";
    gp << "set autoscale yfix\n";
    gp << "set autoscale cbfix\n";
    gp << "splot '-'\n";
    gp.send2d(frame);
    gp.flush();
    return 0;
}   


int greaficar_vector(float *vector, int longitud){
    float frame[LONGITUD];
    for (int n=0; n<longitud; n++){
            frame[n]=*(vector +n);
    }

    Gnuplot gpV;
    gpV << "unset key\n";
    gpV << "set autoscale yfix\n";
    gpV << "set xrange [ -1 : 1000000 ] \n";
    gpV << "plot '-'\n";
    gpV.send1d(frame);
    gpV.flush();
    return 0;
}

int imprimir(float *red, int dim){
	int i,j;
	for(i=0;i<dim;i++){
		for(j=0;j<dim;j++){
			if(*(red+dim*i+j)<10){printf("%.2f   ",*(red+dim*i+j));}
			else{printf("%.2f  ",*(red+dim*i+j));}
		}	
	printf("\n");
	}
    printf("\n\n");
return 0;
}
