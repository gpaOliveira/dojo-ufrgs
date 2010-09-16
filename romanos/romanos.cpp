



#include "romanos.h"

std::string getRoma(int n){
	std::string result;
	
	switch(n)
	{	
		case 4: result = "IV"; n-= 4; break;
		case 7:
		case 6:
		case 5: result = "V"; n -= 5; break;
		case 10: result = "X"; n -= 10; break;
		case 42: result = "XL"; n -= 40; break;		
		case 50: result = "L"; n -= 50; break;
		case 100: result = "C"; n -= 100; break;
		case 500: result = "D"; n -= 500; break;
		case 1000: result = "M"; n -= 1000; break;
	}

	while(n){
		result += "I";
		n--;
	}

	return result;
}

std::string decimalToRomano(int n)
{
	std::string result = "";
	int qtdUnidades;
	int qtdDezenas;
	int qtdCentenas;
	int qtdMilhares;	
	
	qtdUnidades = n%10;
	n = n/10;
	qtdDezenas = n%10;
	n /= 10;
	qtdCentenas = n%10;
	n /= 10;
	qtdMilhares = n%10;
	
	result = result + getRoma(qtdUnidades);
	result = result + getRoma(qtdDezenas);

	return result;
}
