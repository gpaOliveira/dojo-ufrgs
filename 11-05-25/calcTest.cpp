
#include "test.h"
#include "calc.h"

START_TESTS()

	START_TEST("testa soma 2 numeros")		
		ASSERT( calculadora("2 + 2") == 4 );
		ASSERT( calculadora("3 + 3") == 6 );
	END_TEST()

	START_TEST("testa subtração 2 numeros")
		ASSERT( calculadora("2 - 2") == 0 );
		ASSERT( calculadora("9 - 15") == -6 );
	END_TEST()


	START_TEST("TESTA DIVISAO DE DOIS NUMEROS")
        ASSERT ( calculadora("2 / 2") == 1 );
		ASSERT ( calculadora("3 / 2") == (3./2));
		ASSERT ( calculadora("5 / 0") == 1/0.0);
	END_TEST()

	START_TEST("testa multiplicação 2 numeros")
		ASSERT( calculadora("5 * 5") == 25);
	END_TEST()

	START_TEST("testa atribuicao")
        calculadora("x= 10");
		ASSERT( calculadora("x") == 10);
		calculadora("y= 42");
		ASSERT( calculadora("y") == 42);
		ASSERT( calculadora("x") == 10);
    END_TEST()

	START_TEST("testa atribuicao e operacao")
		calculadora("x= 10");
		calculadora("y= 42");
		ASSERT( calculadora("x + y") == 52);
		ASSERT( calculadora("x + 10") ==20);	
	END_TEST()

END_TESTS()
