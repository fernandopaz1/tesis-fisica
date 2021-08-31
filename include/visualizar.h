#include <vector>
#include <cmath>
#include <boost/tuple/tuple.hpp>
#include "gnuplot-iostream.h"

const int DIM = 60;

int graficar(float *red, int dim);
int imprimir(float *red, int dim);


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
