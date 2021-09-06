#include "random.h"

int perturbar_nodo_aleatorio(float *red, int dim, float sigma1,float sigma2);
int limpiar_red(float *red, int dim);
float energia_total(float *red, int dim);
float suma_vecinos(float *red, int dim, int i, int j);
bool es_nodo_borde(int dim, int i, int j);
int actualizar_red(float *red_dest, float *red_orig, int dim);
bool es_nodo_borde(int dim, int i, int j);
int limpiar_red(float *red, int dim);
int aumentar_vecinos(float *red, int dim, int i, int j, float cantindad);
float campo_medio(float *red, int dim);



int perturbar_nodo_aleatorio(float *red, int dim,float sigma1, float sigma2){
    int i= entero_aleatorio(0, dim-1);
    int j= entero_aleatorio(0, dim-1);
    *(red+i*dim+j)=campo_aleatoro(sigma1,sigma2);
    return 0;
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

float energia_total(float *red, int dim){
    int i,j;
    float B_tot=0.0;

    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            B_tot+=(*(red+i*dim+j))*(*(red+i*dim+j));
        }
    }

    return B_tot/(1.0*(dim*dim));
}

float campo_medio(float *red, int dim){
    int i,j;
    float B_tot=0.0;

    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            B_tot+=*(red+i*dim+j);
        }
    }

    return B_tot/(1.0*(dim*dim));
}

float suma_vecinos(float *red, int dim, int i, int j){
    if(i==0){
        if(j==0){
            return  *(red+(i+1)*dim+j)+*(red+i*dim+j+1);
        }
        return *(red+(i+1)*dim+j)+*(red+i*dim+j-1)+*(red+i*dim+j+1); 
    }
    if(j==0){
        return *(red+(i-1)*dim+j)*+*(red+(i+1)*dim+j)+*(red+i*dim+j+1);
    }
    if(i==(dim-1)){
        if(j==(dim-1)){
            return *(red+(i-1)*dim+j)*+*(red+i*dim+j-1);
        }
    }
    if(j==(dim-1)){
         return *(red+(i-1)*dim+j)*+*(red+(i+1)*dim+j)+*(red+i*dim+j-1);
    }
    return *(red+(i-1)*dim+j)*+*(red+(i+1)*dim+j)+*(red+i*dim+j-1)+*(red+i*dim+j+1);
}

int aumentar_vecinos(float *red, int dim, int i, int j, float cantindad){
    if(i != 0){
        *(red+(i-1)*dim+j)+=cantindad;
    }
    if(i != (dim-1)){
        *(red+(i+1)*dim+j)+=cantindad;
    }
    if(j != 0){
        *(red+i*dim+j-1)+=cantindad;
    }
    if(j != (dim-1)){
        *(red+i*dim+j+1)+=cantindad;
    }
    return 0;
}

bool es_nodo_borde(int dim, int i, int j){
    return (i==0) || (i==(dim-1)) || (j==0) || (j==(dim-1));
}

int actualizar_red(float *red_dest, float *red_orig, int dim){
    int i,j;
    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            *(red_dest+i*dim+j)=*(red_dest+i*dim+j)+*(red_orig+i*dim+j);
            *(red_orig+i*dim+j)=0.0;
        }
    }
    return 0;
}