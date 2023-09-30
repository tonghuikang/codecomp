#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

const long long val = 1LL << 32;

pair<long long, long long> decode(long long z) {
    return make_pair(z / val, z % val);
}

long long encode(long long x, long long y) {
    return x * val + y;
}

int solve(int a, int b, int c, int d, int m) {
    unordered_map<long long, int> dist;
    dist[encode(a,b)] = 0;

    queue<pair<int, int>> queue;
    queue.push(make_pair(a, b));

    while (!queue.empty()) {
        pair<int, int> p = queue.front();
        queue.pop();
        int x = p.first, y = p.second;
        int cnt = dist[encode(x,y)];

        int xx = x & y, yy = y;
        if (dist.count(encode(xx, yy)) == 0) {
            queue.push(make_pair(xx, yy));
            dist[encode(xx, yy)] = cnt + 1;
        }

        xx = x | y, yy = y;
        if (dist.count(encode(xx, yy)) == 0) {
            queue.push(make_pair(xx, yy));
            dist[encode(xx, yy)] = cnt + 1;
        }

        xx = x, yy = x ^ y;
        if (dist.count(encode(xx, yy)) == 0) {
            queue.push(make_pair(xx, yy));
            dist[encode(xx, yy)] = cnt + 1;
        }

        xx = x, yy = y ^ m;
        if (dist.count(encode(xx, yy)) == 0) {
            queue.push(make_pair(xx, yy));
            dist[encode(xx, yy)] = cnt + 1;
        }
    }
    
    if(dist.count(encode(c,d)) > 0)
        return dist[encode(c,d)];
    
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