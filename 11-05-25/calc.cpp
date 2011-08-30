#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "calc.h"

double aritmetica( int num1, int num2, char oper)
{
	double resultado; 


	switch (oper) 
	{
		case '+':
			 resultado = num1+num2;
			break;
		case '-':
			resultado = num1-num2;
			break;
		case  '/':
            resultado = (double) num1/num2;
            break;
		case '*':
			resultado = num1*num2;
			break;
	}

	return resultado;
}


double calculadora(const char* exp)
{
	int numOp;
	char n1[200], n2[200];
	int num1, num2;	
	char oper, oper_str[200], var, testeIgual;

	numOp = sscanf(exp,"%s %s %s", n1, oper_str, n2);

	switch(numOp) {
		case 3:
			num1 = atoi(n1);
			if (num1 == 0)
            	if (n1[0] =='0')   
                	num1 = 0;            
               	else
					num1 = memoria[n1[0]-'a'];
			
			num2 = atoi(n2);
				if (num2 == 0)
		        	if (n2[0] =='0')   
		            	num2 = 0;            
		           	else
						num2 = memoria[n2[0]-'a'];

			return aritmetica(num1, num2, oper_str[0]);
		case 2: 
		{
			// X= 10
			char var = n1[0]; // X=
			int num = atoi(oper_str); // 10
			memoria[var-'a'] = num;
			break;
		}
		case 1:
			char var = n1[0];
			return memoria[var-'a'];
	}
}
