#include "visualizar.h"
#include "operacion-redes.h"

#include "constantes.h"

int soc_generator(int dim);

int soc_generator(int dim){
    int i,j,k, t;
    float *red, Z_c, sigma1, sigma2, e, g, Z_k;
    int T_Final=1000000;
    float *c;

    int s=2*D+1;
    sigma1=-0.2;
    sigma2=0.8;
    Z_c=5.0;



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
                    *(c+i*dim+j)=*(c+i*dim+j)-(2*D/s)*Z_c;
                    aumentar_vecinos(c,dim,i,j,Z_c/s);
                    g=(2*D/s)*(2*abs(Z_k)/Z_c-1)*Z_c*Z_c;
                    e+=g;
                }
            }
        }
        if(e>0){
            actualizar_red(red,c,dim);
        }else{
            perturbar_nodo_aleatorio(red,dim,sigma1,sigma2);
        }        
    }
    printf("%d\n", t);
    graficar(red,dim);
    free(red);
    return 0;
}


