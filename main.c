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
int imprimir(float *red, int dim);

int main(int argc,char *argv[]){

    double total_time;
	clock_t start, end;
	start = clock();

    srand(31); 
    
    soc_generator(10);

    end = clock();
	//time count stops 
    total_time = ((((double)(end - start)) / (double)CLOCKS_PER_SEC));	
    printf("\nEl tiempo (segundos) requerido es:  %lf \n", total_time);	

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

float suma_vecinos(float *red, int dim, int i, int j){
    if(es_nodo_borde(dim,i,j)){
        return 0.0;
    }
    return *(red+(i-1)*dim+j)+*(red+(i+1)*dim+j)+*(red+i*dim+j-1)+*(red+i*dim+j+1);
}

float aumentar_vecinos(float *red, int dim, int i, int j, float cantindad){
    if(es_nodo_borde(dim,i,j)){
        return 0.0;
    }
    *(red+(i-1)*dim+j)+=cantindad;
    *(red+(i+1)*dim+j)+=cantindad;
    *(red+i*dim+j-1)+=cantindad;
    *(red+i*dim+j+1)+=cantindad;
}

bool es_nodo_borde(int dim, int i, int j){
    return i==0 || i==dim-1 || j==0 || j==dim-1;
}

int copiar_red(float *red_dest, float *red_orig, int dim){
    int i,j;
    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            *(red_dest+i*dim+j)=*(red_orig+i*dim+j);
            *(red_orig+i*dim+j)=0.0;
        }
    }
}

int soc_generator(int dim){
    int i,j,k, t;
    float *red, Z_c, sigma1, sigma2, e, g, Z_k;
    int T_Final=100;
    float *c;

    int s=2*D+1;

    red=(float*)malloc((dim*dim)*sizeof(float));
    c=(float*)malloc((dim*dim)*sizeof(float));

    // limpiar_red(red,dim);

    for(t=0;t<T_Final;t++){
        e=0.0;
        for(i=0;i<dim;i++){
            for(j=0;j<dim;j++){
                g=0.0;
                Z_k= *(red+i*dim+j)-1/(2*D)*suma_vecinos(red,dim,i,j);
                if(abs(Z_k)>Z_c){
                    *(c+i*dim+j)-=(2*D/s)*Z_c;
                    suma_vecinos(red,dim,i,j, Z_c/s);
                    g=(2*D/s)*(2*abs(Z_k)/Z_c-1)*Z_c*Z_c;
                    e+=g;
                }
            }
        }
        if(e>0){
            copiar_red(red,c,dim);
        }
    }

    free(red);
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