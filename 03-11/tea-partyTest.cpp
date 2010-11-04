
#include "tests.h"
#include "tea-party.h"

START_TESTS()

	//um teste
	START_TEST("Recebe Padawan que eh homem e nao eh Knight e retorna \"Hello Mr. Padawan\" ")
		ASSERT(welcome("Padawan", false, false) == "Hello Mr. Padawan" )	

	END_TEST()

	START_TEST("Recebe Newton que eh homem e eh Knight e retorna \"Hello Sir Newton\" ")
		ASSERT(welcome("Newton", false, true) == "Hello Sir Newton")

	END_TEST()

	START_TEST("Recebe Elizabeth que eh mulher e nao eh Knight e retorna \"Hello Ms. Elizabeth\" ")
		ASSERT(welcome("Elizabeth", true, false) == "Hello Ms. Elizabeth")
	END_TEST()

	START_TEST("Recebe Vania que eh mulher e eh Knight e retorna \"Hello Ms. Vania\" ")
		// heuehuehueheu		
		ASSERT(welcome("Vania", true, true) == "Hello Ms. Vania")
	
	END_TEST()




END_TESTS()
