#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;
const int MAX_N = 1000100;
ll a[MAX_N];
ll b[MAX_N];
ll atack[MAX_N];
ll psum[MAX_N];
ll dp[MAX_N];
int front;
int top;

void insert(ll newa, ll newb) {
    a[top + 1] = newa;
    b[top + 1] = newb;
    while (top > 0 &&
           (a[top] - a[top - 1]) * (b[top + 1] - b[top - 1]) > (a[top + 1] - a[top - 1]) * (b[top] - b[top - 1])) {
        --top;
        a[top + 1] = newa;
        b[top + 1] = newb;
    }
    ++top;
}

ll f(int k, int x) {
    return a[k] * x + b[k];
}

ll query(int x) {
    while (front < top && f(front, x) <= f(front + 1, x)) ++front;
    return f(front, x);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, a, b, c;
    cin >> n >> a >> b >> c;
    psum[0] = 0;
    for (int i = 0; i < n; ++i) {
        cin >> atack[i];
        psum[i + 1] = psum[i] + atack[i];
    }
    for (int i = 1; i < n + 1; ++i) {
        dp[i] = query(psum[i]) + a * (psum[i] * psum[i]) + b * psum[i] + c;
        insert(-2 * a * psum[i], dp[i] + a * (psum[i] * psum[i]) - b * psum[i]);
    }
    cout << dp[n];

}