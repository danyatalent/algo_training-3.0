#include <iostream>
#include<vector>

using namespace std;

vector<vector<int>> g;
vector<int> used, top;
int flag = 0;

void dfs(int v) {
    used[v] = 1;
    for (int i = 0; i < g[v].size(); i++) {
        int to = g[v][i];
        if (used[to] == 1) flag = 1;
        if (used[to] == 0) dfs(to);
    }
    used[v] = 2;
    top.push_back(v);
}

int main()
{
    int n, m;
    cin >> n >> m;
    g.resize(n + 1); used.resize(n + 1);
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }
    for (int i = 1; i <= n; i++) {
        if (used[i] == 0) dfs(i);
    }
    if (flag == 1) cout << -1;
    else {
        for(int i = top.size() - 1; i >= 0; i--) {
            cout << top[i] << ' ';
        }
    }
    return 0;
}