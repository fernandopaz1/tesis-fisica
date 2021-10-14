#include "parametros.h"
#include "visualizar.h"
#include "operacion-redes.h"
#include "saveCSV.h"
#include "unistd.h"
#include "constantes.h"

void soc_generator();

void soc_generator(){
    int i,j,k, t, *cluster,m=DIM/2;
    float *red, *centro_masa,*c, sigma1, sigma2, e, g, Z_k, P, A,R,E_total_avalancha;
    int nroAv, T, T_Final=ITERACIONES;
    int T_anterior, T_actual, delta_T;


    FILE *fp = fopen("datos.csv", "w+");
    FILE *fp2 = fopen("perfil.csv", "w+");
    FILE *fp3 = fopen("caracterizacion.csv", "w+"); 
    fprintf(fp,"Iteraciones,Energia_liberada,Energia_total\n");
    fprintf(fp3,"nro,T,E,P,A,R\n");
    headerNumerico(fp2, DIM);

    float s=2.0*D+1.0;
    sigma1=-0.2;
    sigma2=0.8;
    float e0=(2.0*D/s)*Z_c*Z_c;


    red=(float*)malloc((DIM*DIM)*sizeof(float));
    c=(float*)malloc((DIM*DIM)*sizeof(float));
    centro_masa=(float*)malloc(2*sizeof(float));
    cluster=(int*)malloc((DIM*DIM)*sizeof(int));
    limpiar_red(red,DIM);
    limpiar_red(c,DIM);
    limpiar_red(cluster,DIM);

    if(cargar_red(red, DIM)){
        printf("%s\n","Se cargó red");
    }else{
        printf("%s\n","No  se pudo cargar red");
    }

    T=0;
    nroAv=0;
    E_total_avalancha=0.0;
    P=0.0;
    A=0.0;
    R=0.0;
    T_anterior=0;
    T_actual=0;
    delta_T=0;
    float e_anterior=0.0;

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
                    agregar_cluster(cluster, DIM, i,j);
                }
            }
        }
        if(e>0.0){
            actualizar_red(red,c,DIM);
            T_actual=t;
            T++;
            E_total_avalancha+=e;
            P= (e>P) ? e : P;
        }else{
            if(T!=0 && e_anterior!=0.0){
                A=calcular_centro_de_masa(cluster, centro_masa,DIM);
                R= calcular_radio(cluster, centro_masa, DIM);
                fprintf(fp3,"%d,%d,%f,%f,%f,%f\n",nroAv,T,E_total_avalancha/e0,P/e0,A,R);
                T=0;A=0.0;P=0.0;R=0.0;nroAv++;E_total_avalancha=0.0;
                limpiar_red(cluster,DIM);
            }
            perturbar_nodo_aleatorio(red,DIM,sigma1,sigma2);
        }

        fprintf(fp,"%d,%lf,%lf\n", t,e/e0,energia_total(red, DIM)/e0);
        
        if( t % 20000 == 0){ 
            saveLinea(fp2, red, DIM);
        }
        e_anterior=e;
    }

    guardar_red(red, DIM);    
    // graficar(red,DIM);

    free(red);
    red=NULL;
    free(c);
    c=NULL;
    fflush(fp);
    fclose(fp);
    fflush(fp2);
    fclose(fp2);
    fflush(fp3);
}


