#include "parametros.h"
#include "visualizar.h"
#include "operacion-redes.h"
#include "saveCSV.h"
#include "unistd.h"
#include "constantes.h"

void soc_generator();

void soc_generator()
{

	int i, j, k, t, m = DIM / 2;
	float *red, *c, *e_r, *e_tot, sigma1, sigma2, e, g, Z_k, *P, *E_total_avalancha;
	int nroAv, *T, T_Final = ITERACIONES;
	int T_anterior, T_actual, delta_T;

	float s = 2.0 * D + 1.0;
	sigma1 = -0.2;
	sigma2 = 0.8;
	float e0 = (2.0 * D / s) * Z_c * Z_c;
	int T_max_av = (int)T_Final / 2;

	red = (float *)malloc((DIM * DIM) * sizeof(float));
	c = (float *)malloc((DIM * DIM) * sizeof(float));
	e_r = (float *)malloc(T_Final * sizeof(float));
	e_tot = (float *)malloc(T_Final * sizeof(float));

	limpiar_red(red, DIM);
	limpiar_red(c, DIM);

	if (cargar_red(red, DIM,filename))
	{
		printf("%s\n", "Se cargó red");
	}
	else
	{
		printf("%s\n", "No  se pudo cargar red");
	}

	nroAv = 0;
	E_total_avalancha = (float *)malloc(T_max_av * sizeof(float));
	P = (float *)malloc(T_max_av * sizeof(float));
	T = (int *)malloc(T_max_av * sizeof(int));
	T_anterior = 0;
	T_actual = 0;
	delta_T = 0;
	float e_anterior = 0.0;

	for (t = 0; t < T_Final; t++)
	{	
		e = 0.0;
		for (i = 0; i < DIM; i++)
		{
			for (j = 0; j < DIM; j++)
			{
				Z_k = *(red + i * DIM + j) - (1.0 / (2.0 * D)) * suma_vecinos(red, DIM, i, j);
				if (Z_k > Z_c)
				{
					*(c + i * DIM + j) -= (2.0 * D / s) * Z_c;
					aumentar_vecinos(c, DIM, i, j, Z_c / s);
					g = (2 * D / s) * ((2.0 * Z_k / Z_c) - 1.0) * Z_c * Z_c;
					e += g;
				}
			}
		}
		if (e > 0.0)
		{
			actualizar_red(red, c, DIM);
			*(T + nroAv) = *(T + nroAv) + 1;
			*(E_total_avalancha + nroAv) += e;
			*(P + nroAv) = (e > *(P + nroAv)) ? e : *(P + nroAv);
		}
		else
		{
			if (*(T + nroAv) != 0 && e_anterior != 0.0)
			{
				*(E_total_avalancha + nroAv) = *(E_total_avalancha + nroAv) / e0;
				*(P + nroAv) = *(P + nroAv) / e0;
				nroAv++;
				*(E_total_avalancha + nroAv) = 0.0;
				*(P + nroAv) = 0.0;
				*(T + nroAv) = 0;
			}
			perturbar_nodo_aleatorio(red, DIM, sigma1, sigma2);
		}

		*(e_r + t) = e / e0;
		*(e_tot + t) = energia_total(red, DIM) / e0;

		e_anterior = e;
	}

	guardar_red(red, DIM, filename);
	// save_energies(e_r, e_tot, T_Final);
	save_avalancha(T, E_total_avalancha, P, nroAv);
	saveLinea(red,DIM);

	free(red);
	free(c);
	free(e_r);
	free(e_tot);
	free(E_total_avalancha);
	free(P);
	free(T);
}
