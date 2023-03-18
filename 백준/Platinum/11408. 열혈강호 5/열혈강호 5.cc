#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

const int MAX_V = 803;
const int SOURCE = 801;
const int SINK = 802;
const int INF = 987654321;

int capacity[MAX_V][MAX_V];
int flow[MAX_V][MAX_V];
int cost[MAX_V][MAX_V];


int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(MAX_V, vector<int>());
    for (int worker = 1; worker <= n; ++worker) {
        capacity[SOURCE][worker] = 1;
        adj[SOURCE].push_back(worker);
        adj[worker].push_back(SOURCE);
    }
    for (int work = 1 + 400; work <= m + 400; ++work) {
        capacity[work][SINK] = 1;
        adj[work].push_back(SINK);
        adj[SINK].push_back(work);
    }
    for (int worker = 1; worker <= n; ++worker) {
        int count;
        cin >> count;
        for (int i = 0; i < count; ++i) {
            int workNum, workCost;
            cin >> workNum >> workCost;
            workNum += 400;

            adj[worker].push_back(workNum);
            adj[workNum].push_back(worker);

            cost[worker][workNum] = workCost;
            cost[workNum][worker] = -workCost;

            capacity[worker][workNum] = 1;
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
            flow[parent[t]][t] += maxFlow;
            flow[t][parent[t]] -= maxFlow;
        }
        ++count;
    }

    cout << count << endl;
    cout << minCost << endl;

}


