#include <unistd.h>


void headerNumerico(FILE *f, int n);
void saveLinea(FILE *f, float *red, int dim);
void guardar_red(float *red, int dim);
int existe_archivo(char *nombre);
bool cargar_red(float *red,int dim);

void headerNumerico(FILE *f, int n) {
    for(int k=0;k<n;k++){
        fprintf(f,"%d",k+1);
        if(k<n-1){
            fprintf(f,",");
        }else{
            fprintf(f,"\n");
        }
    }
}

void saveLinea(FILE *f, float *red, int dim){
    int m=dim/2;
    for(int k=0;k<dim;k++){
        fprintf(f,"%f",*(red+m*dim+k));
        if(k<dim-1){
            fprintf(f,",");
        }else{
            fprintf(f,"\n");
        }
    }
}

int existe_archivo(char *nombre){
    return access(nombre, F_OK) == 0;
}

void guardar_red(float *red, int dim){
    char filename[sizeof "data/red_equilibrio100.csv"];
    sprintf(filename, "data/red_equilibrio%03d.csv", dim);

    if(existe_archivo(filename) ){
        FILE *red_equilibrio = fopen(filename, "w+");    
        for(int i=0; i<dim; i++){
            for(int j=0; j<dim; j++){
                if(j==dim-1 && i!=dim-1){
                    fprintf(red_equilibrio,"%f,",*(red+i*dim+j));
                }else if(j==dim-1){
                    fprintf(red_equilibrio,"%f",*(red+i*dim+j));
                }else{
                    fprintf(red_equilibrio,"%f,",*(red+i*dim+j));
                }
            }
        }
        fclose(red_equilibrio);
    } 
}

bool cargar_red(float *red,int dim){
    char buffer[10*dim*dim*sizeof(float)+dim*dim*sizeof(char)], *eof;
    char filename[sizeof "data/red_equilibrio100.csv"];
    sprintf(filename, "data/red_equilibrio%03d.csv", dim);
    if(existe_archivo(filename) ){
        FILE *red_equilibrio= fopen(filename, "r");
        for(int i=0; i<dim; i++){
            for(int j=0; j<dim; j++){
                if(j==dim-1 && i==dim-1){
                    fscanf(red_equilibrio, "%f", red+dim*i+j);
                }else{
                    fscanf(red_equilibrio, "%f,", red+dim*i+j);
                }
            }
        }
        fclose(red_equilibrio); 
        return true;
    }else{
        return false;
    }
}


