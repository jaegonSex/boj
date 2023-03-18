#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

const int price[][5] = {{10, 8, 7, 5, 1},
                        {8,  6, 4, 3, 1},
                        {7,  4, 3, 2, 1},
                        {5,  3, 2, 2, 1},
                        {1,  1, 1, 1, 0}};
const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

const int MAX_V = 2503;
const int SOURCE = 2501;
const int SINK = 2502;
const int INF = 987654321;

int capacity[MAX_V][MAX_V];
int flow[MAX_V][MAX_V];
int cost[MAX_V][MAX_V];
int toIdx(int c){
    if (c=='A') return 0;
    if (c=='B') return 1;
    if (c=='C') return 2;
    if (c=='D') return 3;
    if (c=='F') return 4;
    return 0;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(MAX_V, vector<int>());
    vector<string> tofu(n);
    for (int i = 0; i < n; ++i) {
        cin >> tofu[i];
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int idx = m * i + j;
            if ((i + j) % 2 == 0) {

                adj[SOURCE].push_back(idx);
                adj[idx].push_back(SOURCE);

                capacity[SOURCE][idx] = 1;

                for (int k = 0; k < 4; ++k) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                        int nidx = m * nx + ny;

                        adj[idx].push_back(nidx);
                        adj[nidx].push_back(idx);

                        capacity[idx][nidx] = 1;

                        int p = price[toIdx(tofu[i][j])][toIdx(tofu[nx][ny])];

                        cost[idx][nidx] = -p;
                        cost[nidx][idx] = p;
                    }
                }
            }
            adj[idx].push_back(SINK);
            adj[SINK].push_back(idx);
            capacity[idx][SINK] = 1;
        }
    }


    int minCost = 0;
    int count = 0;
    while (true) {
        int parent[MAX_V];
        int dist[MAX_V];
        bool inQ[MAX_V];
        fill(dist, dist + MAX_V, INF);
        fill(parent, parent + MAX_V, -1);
        fill(inQ, inQ + MAX_V, false);
        queue<int> q;
        q.push(SOURCE);
        inQ[SOURCE] = true;
        dist[SOURCE] = 0;

        while (!q.empty()) {
            int here = q.front();
            q.pop();
            inQ[here] = false;
            for (int i = 0; i < adj[here].size(); ++i) {
                int there = adj[here][i];
                if (capacity[here][there] - flow[here][there] > 0
                    && dist[there] > dist[here] + cost[here][there]) {
                    dist[there] = dist[here] + cost[here][there];
                    parent[there] = here;
                    if (!inQ[there]) {
                        q.push(there);
                        inQ[there] = true;
                    }
                }
            }
        }
        if (parent[SINK] == -1) {
            break;
        }
        int maxFlow = INF;
        for (int t = SINK; t != SOURCE; t = parent[t]) {
            maxFlow = min(maxFlow, capacity[parent[t]][t] - flow[parent[t]][t]);
        }
        for (int t = SINK; t != SOURCE; t = parent[t]) {
            minCost += cost[parent[t]][t] * maxFlow;
            flow[parent[t]][t] ++;
            flow[t][parent[t]] --;
        }
        ++count;
    }


    cout << -minCost << endl;

}


