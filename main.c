#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int rand(void);
float aleatorio(void);
int soc_generator(int dim);

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

int soc_generator(int dim){
    int i,j,k, t, D;
    float *red, Z_c, sigma1, sigma2;
    int T_Final=100;
    D=2;

    int s=2*D+1;

    red=(float*)malloc((dim*dim)*sizeof(float));

    for(t=0;t<T_Final;t++){
        for(i=0;i<dim;i++){
            for(j=0;j<dim;j++){
                *(red+dim*i+j)=aleatorio();
                printf("Aleatorio %d numero %lf\n",dim*i+j,*(red+dim*i+j));
            }
        }
    }

    free(red);
    return 0;
}