#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;


struct Point {
    int idx;
    long long x, y;
};

int C, N;
vector<Point> points;

long long ccw(Point p1, Point p2, Point p3) {
    return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y);
}

long long dist(const Point &p1, const Point &p2) {
    long long dx = p1.x - p2.x;
    long long dy = p1.y - p2.y;
    return dx * dx + dy * dy;
}

bool comp(Point p1, Point p2) {
    long long c = ccw(points[0], p1, p2);
    if (c == 0) return dist(points[0], p1) < dist(points[0], p2);
    return c > 0;
}

vector<Point> convexHull() {
    int minIdx = 0;
    for (int i = 1; i < N; ++i) {
        if (points[i].y < points[minIdx].y || (points[i].y == points[minIdx].y && points[i].x < points[minIdx].x)) {
            minIdx = i;
        }
    }
    swap(points[0], points[minIdx]);

    sort(points.begin() + 1, points.end(), comp);
    vector<Point> ret;
    for (int i = 0; i < N; ++i) {
        ret.push_back(points[i]);
    }
    return ret;
}

void reverseTail(vector<Point> &ch) {
    int reverseIdx = N - 1;
    for (int i = N - 1; i >= 0; --i) {
        if (ccw(points[0], points[i], points[i - 1])) break;
        reverseIdx--;
    }
    reverse(ch.begin() + reverseIdx, ch.end());
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> C;
    while (C--) {
        cin >> N;
        Point point;
        int idxCounter = 0;
        points = vector<Point>();
        for (int i = 0; i < N; ++i) {
            point.idx = idxCounter++;
            cin >> point.x >> point.y;
            points.push_back(point);
        }
        vector<Point> ch = convexHull();
        reverseTail(ch);
        for (int i = 0; i < ch.size(); ++i) {
            cout << ch[i].idx << " ";
        }
        cout << '\n';
    }
}