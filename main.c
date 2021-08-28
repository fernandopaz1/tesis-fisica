#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include <stdbool.h>

#define D 2 

int rand(void);
float aleatorio(void);
int soc_generator(int dim);
float campo_medio(float *red, int dim);
bool es_nodo_borde(int dim, int i, int j);
int limpiar_red(float *red, int dim);

int main(int argc,char *argv[]){

    srand(31); 
    
    soc_generator(4);

    return 0;
}


float aleatorio(void){
	float a;
	a=((float)rand())/((float)RAND_MAX);
	return a;
}

int limpiar_red(float *red, int dim){
    int i,j;

    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            *(red+i*dim+j)=0.0;
        }
    }

    return 0;
}

float campo_medio(float *red, int dim){
    int i,j,B_tot=0;

    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            B_tot+=*(red+i*dim+j);
        }
    }

    return B_tot/(dim*dim);
}

bool es_nodo_borde(int dim, int i, int j){
    return i==0 || i==dim-1 || j==0 || j==dim-1;
}

int soc_generator(int dim){
    int i,j,k, t;
    float *red, Z_c, sigma1, sigma2;
    int T_Final=100;

    int s=2*D+1;

    red=(float*)malloc((dim*dim)*sizeof(float));

    limpiar_red(red,dim);

    for(t=0;t<T_Final;t++){
        for(i=0;i<dim;i++){
            for(j=0;j<dim;j++){
                if(!es_nodo_borde(dim,i,j)){
                    *(red+dim*i+j)=aleatorio();
                }
                printf("Aleatorio %d numero %lf\n",dim*i+j,*(red+dim*i+j));
            }
        }
    }


    printf("El 0,0 es borde %d: ", es_nodo_borde(dim,0,0));

    free(red);
    return 0;
}

