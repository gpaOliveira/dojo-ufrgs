#include "tests.h"
#include <string>

using namespace std;

#include "cinzas.h"

int resposta[2] = { -1, -1 };

#define FIRST 0
#define LAST  1

char simples[MAX_WIDTH][MAX_HEIGHT] =
{ 
  { ' ' , ' ', ' ', ' ' },
  { ' ' , '*', 'A', ' ' },
  { ' ' , ' ', ' ', ' ' },
  { ' ' , ' ', ' ', ' ' } 
};

char outra[MAX_WIDTH][MAX_HEIGHT] =
{ 
  { ' ' , ' ', ' ', ' ' },
  { ' ' , '*', ' ', 'A' },
  { ' ' , ' ', ' ', ' ' },
  { ' ' , ' ', ' ', ' ' } 
};

char falha[MAX_WIDTH][MAX_HEIGHT] =
{ 
  { '*' , ' ', ' ', ' ' },
  { ' ' , ' ', ' ', ' ' },
  { ' ' , ' ', ' ', ' ' },
  { ' ' , ' ', ' ', 'A' } 
};

char variosA[MAX_WIDTH][MAX_HEIGHT] =
{ 
  { '*' , ' ', ' ', ' ' },
  { '*' , ' ', 'A', ' ' },
  { ' ' , 'A', ' ', ' ' },
  { ' ' , ' ', ' ', 'A' } 
};

char variosA2[MAX_WIDTH][MAX_HEIGHT] =
{ 
  { '*' , ' ', ' ', ' ' },
  { '*' , ' ', 'A', ' ' },
  { ' ' , ' ', 'A', ' ' },
  { ' ' , ' ', ' ', 'A' } 
};

char variosA3[MAX_WIDTH][MAX_HEIGHT] =
{ 
  { '*' , ' ', ' ', ' ' , ' '},
  { ' ' , ' ', 'A', ' ' , ' '},
  { ' ' , ' ', 'A', ' ' , ' '},
  { ' ' , ' ', ' ', 'A' , 'A'},
  { ' ' , ' ', ' ', ' ' , 'A'}
};

START_TESTS()

    START_TEST("Testa distancia\n")
    
        ASSERT( distanciaGrid(1, 1, 1, 2) == 1 );
        ASSERT( distanciaGrid(0, 0, 3, 4) == 4 );
        ASSERT( distanciaGrid(0, 0, 3, 3) == 3 );
        
    END_TEST()

	START_TEST("Nuvem do lado, 1 dia\n")

        nuvem(simples, 4, 4, resposta);
		ASSERT(  resposta[FIRST] == 1 );

	END_TEST()
	
	START_TEST("Nuvem perto, 2 dias\n")
    
        nuvem(outra, 4, 4, resposta);
		ASSERT( resposta[FIRST] == 2 );

	END_TEST()
	
	START_TEST("Nuvem longe?, 3 dias\n")

        nuvem(falha, 4, 4, resposta);
		ASSERT( resposta[FIRST] == 3 );

	END_TEST()
    
    START_TEST("Varios A?, 1 dias\n")

        nuvem(variosA, 4, 4, resposta);
		ASSERT( resposta[FIRST] == 1 );

	END_TEST()
	
    START_TEST("Varios A2?, 2 dias\n")

        nuvem(variosA2, 4, 4, resposta);
		ASSERT(  resposta[FIRST] == 2 );

	END_TEST()
	
	
    START_TEST("Varios A2?, 2 dias\n")

        nuvem(variosA2, 4, 4, resposta);
		ASSERT(  resposta[LAST] == 3 );

	END_TEST()
	
	START_TEST("Varios A3?, 2 dias\n")

        nuvem(variosA3, 5, 5, resposta);
		ASSERT(  resposta[LAST] == 4 );

	END_TEST()

END_TESTS()

