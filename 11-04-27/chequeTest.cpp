#include "tests.h"
#include <string>

using namespace std;

#include "cheque.h"

START_TESTS()

	START_TEST("Recebe 1 e retorna \"Um real\"")

		ASSERT( chequePorExtenso(1) == "um real" );

	END_TEST()

	START_TEST("Recebe 2 e retorna \"Dois reais\"")

		ASSERT( chequePorExtenso(2) == "dois reais" );

	END_TEST()
	
	START_TEST("Recebe um número e retorna o nome do número")

		ASSERT( numeroPorExtenso(4) == numeros[4] );
		ASSERT( numeroPorExtenso(9) == numeros[9] );

	END_TEST()

	START_TEST("Recebe um número e retorna o número em reais")

		ASSERT( chequePorExtenso(14) == "catorze reais" );
		ASSERT( chequePorExtenso(20) == "vinte reais" );
		ASSERT( chequePorExtenso(21) == "vinte e um reais" );
		ASSERT( chequePorExtenso(22) == "vinte e dois reais" );
	END_TEST()

	START_TEST("LOL")
		ASSERT( chequePorExtenso(32) == "trinta e dois reais" );
		ASSERT( chequePorExtenso(0) == "zero reais" );
		ASSERT( chequePorExtenso(42) == "quarenta e dois reais" );
		ASSERT( chequePorExtenso(19) == "dezenove reais" );

	END_TEST()

	
END_TESTS()

