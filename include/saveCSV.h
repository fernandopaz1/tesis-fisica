#include <unistd.h>

void headerNumerico(FILE *f, int n);
void saveLinea(FILE *f, float *red, int dim);
void guardar_red(float *red, int dim);
int existe_archivo(char *nombre);
bool cargar_red(float *red, int dim);
void save_energies(float *e_r, float *e_tot, int T_Final);
void save_avalancha(int *T, float *e_tot, float *P);

void headerNumerico(FILE *f, int n)
{
	for (int k = 0; k < n; k++)
	{
		fprintf(f, "%d", k + 1);
		if (k < n - 1)
		{
			fprintf(f, ",");
		}
		else
		{
			fprintf(f, "\n");
		}
	}
}

void saveLinea(FILE *f, float *red, int dim)
{
	int m = dim / 2;
	for (int k = 0; k < dim; k++)
	{
		fprintf(f, "%f", *(red + m * dim + k));
		if (k < dim - 1)
		{
			fprintf(f, ",");
		}
		else
		{
			fprintf(f, "\n");
		}
	}
}

int existe_archivo(char *nombre)
{
	return access(nombre, F_OK) == 0;
}

void guardar_red(float *red, int dim)
{
	char filename[sizeof "data/red_equilibrio100.csv"];
	sprintf(filename, "data/red_equilibrio%03d.csv", dim);

	
	FILE *red_equilibrio = fopen(filename, "w+");
	for (int i = 0; i < dim; i++)
	{
		for (int j = 0; j < dim; j++)
		{
			if (j == dim - 1 && i != dim - 1)
			{
				fprintf(red_equilibrio, "%f,", *(red + i * dim + j));
			}
			else if (j == dim - 1)
			{
				fprintf(red_equilibrio, "%f", *(red + i * dim + j));
			}
			else
			{
				fprintf(red_equilibrio, "%f,", *(red + i * dim + j));
			}
		}
	}
	fclose(red_equilibrio);

}

bool cargar_red(float *red, int dim)
{
	char buffer[10 * dim * dim * sizeof(float) + dim * dim * sizeof(char)], *eof;
	char filename[sizeof "data/red_equilibrio100.csv"];
	sprintf(filename, "data/red_equilibrio%03d.csv", dim);
	if (existe_archivo(filename))
	{
		FILE *red_equilibrio = fopen(filename, "r");
		for (int i = 0; i < dim; i++)
		{
			for (int j = 0; j < dim; j++)
			{
				if (j == dim - 1 && i == dim - 1)
				{
					fscanf(red_equilibrio, "%f", red + dim * i + j);
				}
				else
				{
					fscanf(red_equilibrio, "%f,", red + dim * i + j);
				}
			}
		}
		fclose(red_equilibrio);
		return true;
	}
	else
	{
		return false;
	}
}

void save_energies(float *e_r, float *e_tot, int T_Final)
{
	FILE *fp = fopen("datos.csv", "w+");
	fprintf(fp, "Iteraciones,Energia_liberada,Energia_total\n");
	for (int t = 0; t < T_Final; t++)
	{
		fprintf(fp, "%d,%lf,%lf", t, *(e_r + t), *(e_tot + t));
		if (t != T_Final - 1)
		{
			fprintf(fp, "\n");
		}
	}
	fclose(fp);
}

void save_avalancha(int *T, float *e_tot, float *P, int T_Final)
{
	printf("%d",T_Final);
	FILE *fp3 = fopen("caracterizacion.csv", "w+");
	// fprintf(fp3,"nro,T,E,P,A,R\n");
	fprintf(fp3, "nro,T,E,P\n");
	for (int t = 0; t < T_Final; t++)
	{
		fprintf(fp3, "%d,%d,%lf,%lf", t, *(T + t), *(e_tot + t), *(P + t));
		if (t != T_Final - 1)
		{
			fprintf(fp3, "\n");
		}
	}
	fclose(fp3);
}