#include <string>
#include <map>
#include <vector>
#define P make_pair

using namespace std;

typedef pair<int,int> point;

double distance(point p1, point p2);

point magneto( vector<point> pts, int radius, point cursor );
