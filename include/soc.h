#include "parametros.h"
#include "visualizar.h"
#include "operacion-redes.h"

#include "constantes.h"


int soc_generator();
int graficar_matriz(float *red, int dim);


int soc_generator(){
    int i,j, t;
    float *red, *c, Z_c, sigma1, sigma2, e, g, Z_k;
    int T_Final=ITERACIONES;
    FILE *fp = fopen("datos.csv", "w");
    fprintf(fp,"Iteraciones,Energia_liberada,Energia_total\n");
    float s=2.0*D+1.0;
    sigma1=-0.2;
    sigma2=0.8;
    Z_c=0.2;
    float e0=(2.0*D/s)*Z_c*Z_c;


    red=(float*)malloc((DIM*DIM)*sizeof(float));
    c=(float*)malloc((DIM*DIM)*sizeof(float));
    
    limpiar_red(red,DIM);
    limpiar_red(c,DIM);

    graficar_matriz(red,DIM);


    for(t=0;t<T_Final;t++){
        e=0.0;
        for(i=0;i<DIM;i++){
            for(j=0;j<DIM;j++){
                Z_k= *(red+i*DIM+j)-(1.0/(2.0*D))*suma_vecinos(red,DIM,i,j);       
                if(Z_k>Z_c){
                    // printf("El resultado del if es %d con Z_k=%f y Z_c=%f\n",abs(Z_k)>Z_c,abs(Z_k),Z_c);
                    *(c+i*DIM+j)-=(2.0*D/s)*Z_c;
                    aumentar_vecinos(c,DIM,i,j,Z_c/s);
                    g=((2.0*Z_k/Z_c)-1.0);
                    e+=g;
                    // printf("e es %f\n",e);
                }
            }
        }
        if(e>0.0){
            // printf("--------------------Energia %f\n",e);
            actualizar_red(red,c,DIM);
        }else{
            perturbar_nodo_aleatorio(red,DIM,sigma1,sigma2);
        }
        if(t%1000==0){
            fprintf(fp,"%d,%lf,%lf\n", t,e,energia_total(red,DIM)/e0);
        }
        
    }
    free(red);
    free(c);
    free(fp);
    return 0;
}






int graficar_matriz(float *red, int dim){
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
    // gp << "pause 3; refresh; reread;";
    gp.flush();
    return 0;
}   