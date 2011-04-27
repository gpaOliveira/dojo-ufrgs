#include "cheque.h"

using namespace std;

string chequePorExtenso(unsigned int quantia)
{
	string valor;

	valor = numeroPorExtenso(quantia);

		
	if(quantia == 1)
		valor += " real";
	else
		valor += " reais";

	return valor;
}

string numeroPorExtenso(unsigned int quantia)
{
	string valor;
	int dezena, unidade;
	if (quantia <= 19 && quantia >= 0)
		valor = numeros[quantia];
	else {
		dezena = quantia/10;
		unidade = quantia % 10;
		valor = dezenas[dezena-2];
		if(unidade != 0)
			valor += " e " + numeroPorExtenso(unidade);	
	}

	if (quantia < 0 || quantia >= 100)
		valor = " ";

	return valor;
}
