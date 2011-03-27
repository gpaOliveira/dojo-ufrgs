/*

Programa para converter de decimais -> romanos

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

*/

#include "tests.h"
#include "romanos.h"

START_TESTS()

START_TEST("testa 0 retorna STRINGUE vazia")

	ASSERT( decimalToRomano(0) == "");

END_TEST() 

START_TEST("testa 1 retorna I")

	ASSERT( decimalToRomano(1) == "I");

END_TEST()


START_TEST("testa 2 retorna II")

	ASSERT( decimalToRomano(2) == "II");

END_TEST()

START_TEST("testa 3 retorna III")

	ASSERT( decimalToRomano(3) == "III");

END_TEST()

START_TEST("testa 4 retorna IV")

	ASSERT( decimalToRomano(4) == "IV");

END_TEST()

START_TEST("testa 5 retorna V")

	ASSERT( decimalToRomano(5) == "V");

END_TEST()

START_TEST("testa 10 retorna X")

	ASSERT( decimalToRomano(10) == "X");

END_TEST()

START_TEST("testa 42 retorna XLII")
	
	ASSERT( decimalToRomano(42) == "XLII");

END_TEST()

START_TEST ("testa 50 retorna L")

	ASSERT( decimalToRomano(50) == "L");

END_TEST()

START_TEST("testa 100 retorna C")
	
	ASSERT( decimalToRomano(100) == "C");

END_TEST()

START_TEST("testa 500 retorna D")

	ASSERT( decimalToRomano(500) == "D");

END_TEST()

START_TEST("testa 1000 retorna M")

	ASSERT( decimalToRomano(1000) == "M");

END_TEST()


END_TESTS()
