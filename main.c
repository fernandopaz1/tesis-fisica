#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int rand(void);
float aleatorio(void);


int main(int argc,char *argv[]){

    int i=0;
    while(i<1000){
        printf("Aleatorio  %f \n", aleatorio());
        i++;
    }
    return 0;
}


float aleatorio(void){
	float a;
	a=((float)rand())/((float)RAND_MAX);
	return a;
}