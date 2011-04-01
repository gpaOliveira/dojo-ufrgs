#include "tests.h"
#include "paridade.h"

START_TESTS()

	START_TEST("Recebe 1 e retorna paridade 1")

		ASSERT( paridade(1) == 1);		

	END_TEST()

	START_TEST("Recebe 15 e retorna paridade 0")

		ASSERT( paridade(15) == 0);		

	END_TEST()

	START_TEST("Recebe 2 e retorna paridade 1")

		ASSERT( paridade(2) == 1);		

	END_TEST()

	START_TEST("Recebe 12 e retorna paridade 0")

		ASSERT( paridade(12) == 0);		

	END_TEST()

	START_TEST("Recebe 0 e retorna paridade 0")

		ASSERT( paridade(0) == 0);

	END_TEST()

	START_TEST("Recebe -1 e retorna paridade 0")

		ASSERT( paridade(-1) == 0);

	END_TEST()

	START_TEST("Recebe -2 e retorna paridade 1")

		ASSERT( paridade(-2) == 1);

	END_TEST()

END_TESTS()

