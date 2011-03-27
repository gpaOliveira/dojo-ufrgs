#include "tea-party.h"

string welcome(string lastName, bool isWoman, bool isSir)
{
	
	string hello = "Hello ";
	if (isWoman)
		hello+="Ms. ";
	else
		if (isSir)
			hello+="Sir ";
		else
			hello+="Mr. ";

	hello+=lastName;
	return hello;
}
