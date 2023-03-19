#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
const int INF = 987654321;
vector<pair<int, int>> dir = {{1,  0},
                              {0,  1},
                              {-1, 0},
                              {0,  -1}};

int countZero(vector<vector<int>> &office) {
    int zero = 0;
    for (int i = 0; i < office.size(); ++i) {
        for (int j = 0; j < office[0].size(); ++j) {
            if (office[i][j] == 0)++zero;
        }
    }
    return zero;
}

void coverOffice(int x, int y, vector<vector<int>> &office, vector<pair<int, int>> dir, int delta) {
    for (int d = 0; d < dir.size(); ++d) {
        int i = x;
        int j = y;
        while (0 <= i && i < office.size() && 0 <= j && j < office[0].size()) {
            if (office[i][j] == 6) break;
            if (office[i][j] <= 0) office[i][j] += delta;
            i = i + dir[d].first;
            j = j + dir[d].second;
        }
    }
}

int solve(vector<pair<int, int>> &cameras, vector<vector<int>> &office, int index) {
    if (index == cameras.size()) {
        return countZero(office);
    }
    pair<int, int> camera = cameras[index];
    int type = office[camera.first][camera.second];
    int ret = INF;
    if (type == 5) {
        coverOffice(camera.first, camera.second, office, {dir[0], dir[1], dir[2], dir[3]}, -1);
        ret = min(ret, solve(cameras, office, index + 1));
    } else if (type == 4) {
        for (int i = 0; i < 4; ++i) {
            coverOffice(camera.first, camera.second, office, {dir[i % 4], dir[(i + 1) % 4], dir[(i + 2) % 4]}, -1);
            ret = min(ret, solve(cameras, office, index + 1));
            coverOffice(camera.first, camera.second, office, {dir[i % 4], dir[(i + 1) % 4], dir[(i + 2) % 4]}, 1);
        }
    } else if (type == 3) {
        for (int i = 0; i < 4; ++i) {
            coverOffice(camera.first, camera.second, office, {dir[i % 4], dir[(i + 1) % 4]}, -1);
            ret = min(ret, solve(cameras, office, index + 1));
            coverOffice(camera.first, camera.second, office, {dir[i % 4], dir[(i + 1) % 4]}, 1);
        }

    } else if (type == 2) {
        for (int i = 0; i < 4; ++i) {
            coverOffice(camera.first, camera.second, office, {dir[i % 4], dir[(i + 2) % 4]}, -1);
            ret = min(ret, solve(cameras, office, index + 1));
            coverOffice(camera.first, camera.second, office, {dir[i % 4], dir[(i + 2) % 4]}, 1);
        }

    } else {
        for (int i = 0; i < 4; ++i) {
            coverOffice(camera.first, camera.second, office, {dir[i % 4]}, -1);
            ret = min(ret, solve(cameras, office, index + 1));
            coverOffice(camera.first, camera.second, office, {dir[i % 4]}, 1);
        }
    }
    return ret;
}


int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> office(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> office[i][j];
        }
    }

    vector<pair<int, int>> cameras;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (office[i][j] != 0 && office[i][j] != 6) cameras.push_back({i, j});
        }
    }

    int i1 = solve(cameras, office, 0);
    cout << i1;

}


