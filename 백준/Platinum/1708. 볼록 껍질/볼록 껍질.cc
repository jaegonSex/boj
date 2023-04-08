#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

struct Point {
    long long x, y;
};
const int MAX_P = 100000;
int N;
Point points[MAX_P];

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

int convexHullSize() {
    int minIdx = 0;
    for (int i = 1; i < N; ++i) {
        if (points[i].y < points[minIdx].y || (points[i].y == points[minIdx].y && points[i].x < points[minIdx].x)) {
            minIdx = i;
        }
    }
    swap(points[0], points[minIdx]);

    sort(points + 1, points + N, comp);
    stack<Point> st;
    st.push(points[0]);
    st.push(points[1]);
    Point p1, p2;
    for (int i = 2; i < N; ++i) {
        while (st.size() >= 2) {
            p2 = st.top();
            st.pop();
            p1 = st.top();
            if (ccw(p1, p2, points[i]) > 0) {
                st.push(p2);
                break;
            }
        }
        st.push(points[i]);
    }
    return st.size();
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> points[i].x >> points[i].y;
    }
    cout << convexHullSize();
}