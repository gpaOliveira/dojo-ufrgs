#include "magneto.h"
#include <cmath>
#include <climits>
#include <stdio.h>

double distance(int x1, int y1, int x2, int y2)
{
	return sqrt(pow(x1 - x2,2) + pow(y1 - y2,2));
}

point magneto( vector<point> pts, int radius, point cursor )
{
	float minDist = INT_MAX;
	int index;

	for(int i=0; i<pts.size(); i++)
	{
		float dist = distance(pts[i].first,pts[i].second,cursor.first,cursor.second);

		if(dist<minDist) {
			minDist = dist;
			index = i;
		}
	}

	if( minDist<=radius )
		return pts[index];
	else
		return cursor;



}
