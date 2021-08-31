#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include <stdbool.h>
#include "include/soc.h"

int main(int argc,char *argv[]){
    double total_time;
	clock_t start, end;
	start = clock();

    srand(time(NULL));
    // srand(31); 
    soc_generator(60);

    end = clock();
	//time count stops 
    total_time = ((((double)(end - start)) / (double)CLOCKS_PER_SEC));	
    printf("\nEl tiempo (segundos) requerido es:  %lf \n", total_time);	
    return 0;
}