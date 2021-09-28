#include "random.h"

void perturbar_nodo_aleatorio(float *red, int dim, float sigma1,float sigma2);
void limpiar_red(float *red, int dim);
float energia_total(float *red, int dim);
float suma_vecinos(float *red, int dim, int i, int j);
bool es_nodo_borde(int dim, int i, int j);
void actualizar_red(float *red_dest, float *red_orig, int dim);
bool es_nodo_borde(int dim, int i, int j);
void limpiar_red(float *red, int dim);
void aumentar_vecinos(float *red, int dim, int i, int j, float cantindad);
float campo_medio(float *red, int dim);
void agregar_cluster(float *red, int dim, int i, int j);
float calcular_centro_de_masa(int *red, float *centro_masa,int dim);
float calcular_radio(int *red, float *centro_masa,int dim, int *i, int *j);

void perturbar_nodo_aleatorio(float *red, int dim,float sigma1, float sigma2){
    int i= entero_aleatorio(0, dim);
    int j= entero_aleatorio(0, dim);
    *(red+i*dim+j)+=campo_aleatoro(sigma1,sigma2);
}

void limpiar_red(float *red, int dim){
    int i,j;

    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            *(red+i*dim+j)=0.0;
        }
    }

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
    float suma=0.0;
    if(i != 0){
        suma+=*(red+dim*(i-1)+j);
    }
    if(i != dim-1){
        suma+=*(red+dim*(i+1)+j);
    }
    if(j != 0){
        suma+=*(red+dim*i+(j-1));
    }
    if(j != dim-1){
        suma+=*(red+dim*i+(j+1));
    }
    return suma;
}

void aumentar_vecinos(float *red, int dim, int i, int j, float cantindad){
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
}

bool es_nodo_borde(int dim, int i, int j){
    return (i==0) || (i==(dim-1)) || (j==0) || (j==(dim-1));
}

void actualizar_red(float *red_dest, float *red_orig, int dim){
    int i,j;
    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            *(red_dest+i*dim+j)=*(red_dest+i*dim+j)+*(red_orig+i*dim+j);
            *(red_orig+i*dim+j)=0.0;
        }
    }
}

void agregar_cluster(int  *red, int dim, int i, int j){
    *(red+i*dim+j)=1.0;
}


void limpiar_red(int *red, int dim){
    int i,j;
    for(i=0;i<dim;i++){
        for(j=0;j<dim;j++){
            *(red+i*dim+j)=0;
        }
    }
}

float calcular_centro_de_masa(int *red, float *centro_masa,int dim){
    int x=0, y=0, M=0;
    for(int i=0;i<dim;i++){
        for(int j=0;j<dim;j++){
            if(*(red+i*dim+j)){
                x+=i;
                y+=j;
                M++;
            }
        }
    }
    *centro_masa=x/(1.0*M);
    *(centro_masa+1)=y/(1.0*M);
    return 1.0*M;
}

float calcular_radio(int *red, float *centro_masa,int dim){
    float R=0.0;
    int M =0;
    for(int i=0;i<dim;i++){
        for(int j=0;j<dim;j++){
            if(*(red+i*dim+j)){
                R+=fabs((i-*centro_masa)*(i-*centro_masa)+(j-*(centro_masa+1))*(j-*(centro_masa+1)));
                M++;
            }
        }
    }
    return R/(1.0*M);
}