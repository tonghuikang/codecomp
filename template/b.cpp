#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

long long encode(long long x, long long y) {
    return (x << 32) + y;
}

int solve(int a, int b, int c, int d, int m) {
    unordered_map<long long, int> dist;
    dist[encode(a,b)] = 0;

    queue<pair<int, int>> q;
    q.emplace(a, b);

    while (!q.empty()) {
        pair<int, int> p = q.front();
        q.pop();
        int x = p.first, y = p.second;
        int cnt = dist[encode(x,y)];

        vector<pair<int, int>> nextPairs = {
            {x & y, y},
            {x | y, y},
            {x, x ^ y},
            {x, y ^ m}
        };

        for(auto& next : nextPairs) {
            long long encoded = encode(next.first, next.second);
            if (dist.count(encoded) == 0) {
                q.emplace(next.first, next.second);
                dist[encoded] = cnt + 1;
            }
        }
    }
    
    long long encoded = encode(c, d);
    if(dist.count(encoded) > 0)
        return dist[encoded];
    
    return -1;
}

int main() {
    int T, a, b, c, d, m;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> a >> b >> c >> d >> m;
        cout << solve(a, b, c, d, m) << endl;
    }
    return 0;
}