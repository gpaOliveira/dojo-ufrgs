#include <string>
#include <map>
#include <vector>
#define P make_pair

using namespace std;

typedef pair<int,int> point;

double distance(int x1, int y1, int x2, int y2);

point magneto( vector<point> pts, int radius, point cursor );
