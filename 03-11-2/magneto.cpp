#include "magneto.h"
#include <cmath>
#include <climits>
#include <stdio.h>

double distance(point p1, point p2)
{
	return sqrt(pow(p1.first - p2.first,2) + pow(p1.second - p2.second,2));
}

point magneto( vector<point> pts, int radius, point cursor )
{
	float minDist = INT_MAX;
	int index;

	for(int i=0; i<pts.size(); i++)
	{
		float dist = sqrt(pow(pts[i].first - cursor.first,2) + pow(pts[i].second - cursor.second,2));

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
