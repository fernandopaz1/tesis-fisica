#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include <stdbool.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <unistd.h> //para hacer sleep
#include <sys/types.h>
#include <signal.h>
#include "include/soc.h"

sem_t visualizar;


int main(int argc,char *argv[]){
    double total_time;
	clock_t start, end;

    start = clock();
    
	pthread_t thread_1, thread_2;
    sem_init(&visualizar,0,1);

     pthread_create(&thread_1, NULL, *soc_generator, NULL);
    pthread_create(&thread_2, NULL, *graficar_matriz, NULL);
    



    pthread_join(thread_1, NULL);
    pthread_join(thread_2, NULL);
    
	sem_destroy(&visualizar);

    pthread_exit(NULL);


    srand(time(NULL));
    // srand(31); 
    soc_generator();



    end = clock();
	//time count stops 
    total_time = ((((double)(end - start)) / (double)CLOCKS_PER_SEC));	
    printf("\nEl tiempo (segundos) requerido es:  %lf \n", total_time);	
    return 0;
}