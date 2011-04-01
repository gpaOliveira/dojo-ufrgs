#include "paridade.h"
#include <stdio.h>

int main()
{

	int num;
	scanf("%d",&num);

	while (num != 0){
		printf("%d\n",paridade(num));
		scanf("%d",&num);
	}

	return 0;
}
