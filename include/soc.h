#include "parametros.h"
#include "visualizar.h"
#include "operacion-redes.h"

#include "constantes.h"

int soc_generator(int dim);

int soc_generator(int dim){
    int i,j,k, t;
    float *red,*energia, Z_c, sigma1, sigma2, e, g, Z_k;
    int T_Final=ITERACIONES;
    float *c;
    FILE *fp = fopen("datos.csv", "w");
    fprintf(fp,"Iteraciones,Energia_liberada,Energia_total\n");
    float s=2.0*D+1.0;
    sigma1=-0.2;
    sigma2=0.8;
    Z_c=1.0;



    red=(float*)malloc((dim*dim)*sizeof(float));
    c=(float*)malloc((dim*dim)*sizeof(float));
    energia=(float*)malloc((1000000)*sizeof(float));

    // limpiar_red(red,dim);

    for(t=0;t<T_Final;t++){
        e=0.0;
        for(i=0;i<dim;i++){
            for(j=0;j<dim;j++){
                // printf("D es %f y s es %f",D,s);
                Z_k= *(red+i*dim+j)-(1.0/(2.0*D))*suma_vecinos(red,dim,i,j);       
                if(abs(Z_k)>Z_c){
                    *(c+i*dim+j)-=(2.0*D/s)*Z_c;
                    aumentar_vecinos(c,dim,i,j,Z_c/s);
                    g=(2*D/s)*(2.0*abs(Z_k)/Z_c-1.0)*Z_c*Z_c;
                    e+=g;
                    // printf("e es %f\n",e);
                }
            }

        }
        if(e>0){
            // printf("--------------------Energia %f\n",e);
            actualizar_red(red,c,dim);
        }else{
            perturbar_nodo_aleatorio(red,dim,sigma1,sigma2);
        }
            // *(energia+i)=e;
        if(t%100==0){
            fprintf(fp,"%d,%lf,%lf\n", t,e,energia_total(red,dim));
        }
        }
    // printf("%d\n", t);
    // // graficar(red,dim);
    // greaficar_vector(energia,1000000);
    free(red);
    free(fp);
    return 0;
}


