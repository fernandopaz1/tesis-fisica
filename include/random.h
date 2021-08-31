int entero_aleatorio(int a, int b);
float campo_aleatoro(float sigma1, float sigma2);
int rand(void);
float aleatorio(void);

float aleatorio(void){
	float a;
	a=((float)rand())/((float)RAND_MAX);
	return a;
}

int entero_aleatorio(int a, int b){
	int r;
	r=a+(int)((b-a+1)*aleatorio());
	return r;
}

float campo_aleatoro(float sigma1, float sigma2){
    float diferencia = sigma1 - sigma2;
    float r = aleatorio()*diferencia;
    return r + sigma2;
}
