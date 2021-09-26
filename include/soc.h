#include "parametros.h"
#include "visualizar.h"
#include "operacion-redes.h"

#include "constantes.h"

int soc_generator();

int soc_generator(){
    int i,j,k, t,m=DIM/2;
    float *red, *c, Z_c, sigma1, sigma2, e, g, Z_k;
    int T_Final=ITERACIONES;
    FILE *fp = fopen("datos.csv", "w+");
    FILE *fp2 = fopen("perfil.csv", "w+");
    fprintf(fp,"Iteraciones,Energia_liberada,Energia_total\n");

    for(k=0;k<DIM;k++){
        fprintf(fp2,"%d",k+1);
        if(k<DIM-1){
            fprintf(fp2,",");
        }else{
            fprintf(fp2,"\n");
        }
    }    

    float s=2.0*D+1.0;
    sigma1=-0.2;
    sigma2=0.8;
    Z_c=0.2;
    float e0=(2.0*D/s)*Z_c*Z_c;


    red=(float*)malloc((DIM*DIM)*sizeof(float));
    c=(float*)malloc((DIM*DIM)*sizeof(float));

    limpiar_red(red,DIM);
    limpiar_red(c,DIM);
    for(t=0;t<T_Final;t++){
        e=0.0;
        for(i=0;i<DIM;i++){
            for(j=0;j<DIM;j++){
                Z_k= *(red+i*DIM+j)-(1.0/(2.0*D))*suma_vecinos(red,DIM,i,j);       
                if(Z_k>Z_c){
                    *(c+i*DIM+j)-=(2.0*D/s)*Z_c;
                    aumentar_vecinos(c,DIM,i,j,Z_c/s);
                    g=(2*D/s)*((2.0*Z_k/Z_c)-1.0)*Z_c*Z_c;
                    e+=g;
                }
            }
        }
        if(e>0.0){
            actualizar_red(red,c,DIM);
        }else{
            perturbar_nodo_aleatorio(red,DIM,sigma1,sigma2);
        }

        fprintf(fp,"%d,%lf,%lf\n", t,e,energia_total(red, DIM)/e0);
        if( t % 20000 == 0){ 
            int aux= t/20000;
                for(k=0;k<DIM;k++){
                    fprintf(fp2,"%f",*(red+m*DIM+k));
                    if(k<DIM-1){
                        fprintf(fp2,",");
                    }else{
                        fprintf(fp2,"\n");
                    }
                }
 
        }
    }
    graficar(red,DIM);

    free(red);
    red=NULL;
    free(c);
    c=NULL;
    fflush(fp);
    fclose(fp);
    fflush(fp2);
    fclose(fp2);
    return 0;
}


