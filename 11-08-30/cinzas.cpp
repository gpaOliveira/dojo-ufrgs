#include "cinzas.h"

int distanciaGrid(int x1, int y1, int x2, int y2)
{
    int dist_x = fabs(x2 - x1);
    int dist_y = fabs(y2 - y1);
    
    if (dist_x >= dist_y)
        return dist_x;
    else
        return dist_y;
}

void nuvem(char mapa[MAX_WIDTH][MAX_HEIGHT], int w, int h, int retorno[2])
{
    int menor_distancia = MAX_WIDTH;
    int maior_distancia = 0;

    for(int i1=0; i1<w; i1++)
        for(int j1=0; j1<h; j1++)
            if(mapa[i1][j1]=='*')
            {
                for (int i2 = 0; i2 < w; i2++)
                    for (int j2 = 0; j2 < h; j2++)
                        if (mapa[i2][j2] == 'A')
                        {
                            int distancia_agora = distanciaGrid(i1, j1, i2, j2);
                            if (distancia_agora < menor_distancia)
                                menor_distancia = distancia_agora;

                            if (distancia_agora > maior_distancia)
                                maior_distancia = distancia_agora;
                        }
            }
            
    retorno[0] = menor_distancia;
    retorno[1] = maior_distancia;
}

