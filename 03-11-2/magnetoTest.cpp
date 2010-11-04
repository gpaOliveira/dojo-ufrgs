
#include "tests.h"
#include "magneto.h"

START_TESTS()

	vector<point> clean;
	vector<point> one;
	one.push_back( P(50,50) );
	vector<point> two;
	two.push_back( P(50,50) );
	two.push_back( P(100,50) );

	//um teste
	START_TEST("Nao recebe magnet e retorna cursor (25,25)." )

		ASSERT( magneto(clean,5,P(25,25)) == P(25,25) )
		
	END_TEST()
	
	START_TEST("Recebe magnet com ponto (50,50) e retorna cursor (0,0).")
		ASSERT( magneto(one, 5, P(0,0) ) == P(0,0) )

	END_TEST()

	START_TEST("Recebe magnet com (50,50), raio 5, e cursor (49,50) retorna (50,50)")
		ASSERT( magneto(one, 5, P(49,50) ) == P(50,50) )
	END_TEST()


	START_TEST("Recebe magnets com (50,50) e (100,50), e cursor (101,58) e retorna (100,50)")
		ASSERT( magneto(two, 5, P(101,48) ) == P(100,50))
	END_TEST()

/*
	START_TEST("testa distancia (0,0) - (0,1) retorna 1")

		ASSERT(distance(P(0,0) , P(0,1) ) == 1)

	END_TEST()
*/

END_TESTS()
