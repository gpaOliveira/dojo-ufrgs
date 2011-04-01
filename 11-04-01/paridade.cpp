#include "paridade.h"

int paridade(unsigned int num)
{
	int a;
	int cont=0;

	do {
		a = num % 2;
		num = num/2;

		if(a) cont++;	

	} while(num != 0);
	
	return cont % 2;

}
