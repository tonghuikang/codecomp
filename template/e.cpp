#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <set>
using namespace std;

typedef pair<long long, long long> ii; // aliasing for convenience

vector<vector<long long>> read_matrix(long long rows) {
    vector<vector<long long>> ret(rows, vector<long long>(2));
    for (long long i = 0; i < rows; ++i) {
        cin >> ret[i][0] >> ret[i][1];
        ret[i][0]--; ret[i][1]--; // equivalent to minus_one_matrix in python
    }
    return ret;
}

int main() {
    long long T;
    cin >> T;
    while (T--) {
        long long n, m, k;
        cin >> n >> m >> k;
        vector<long long> arr(n);
        for (long long i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        auto mrr = read_matrix(m);
        vector<unordered_set<long long>> g(n), f(n);
        for (auto& edge : mrr) {
            long long a = edge[0], b = edge[1];
            g[a].insert(b);
            f[b].insert(a);
        }

        multiset<long long> sl;
        priority_queue<ii, vector<ii>, greater<ii>> queue;
        vector<ii> droppings;

        for (long long i = 0; i < n; ++i) {
            if (f[i].empty()) {
                queue.push({arr[i] + k, i});
                droppings.push_back({arr[i], i});
            }
        }

        sort(droppings.rbegin(), droppings.rend());

        unordered_map<long long, long long> starts;

        while (!queue.empty()) {
            long long hour, cur;
            tie(hour, cur) = queue.top(); queue.pop();
            starts[cur] = hour;
            sl.insert(hour);
            for (long long nex : g[cur]) {
                f[nex].erase(cur);
                if (f[nex].empty()) {
                    if (arr[nex] >= arr[cur]) {
                        queue.push({(hour / k) * k + arr[nex], nex});
                    } else {
                        queue.push({(hour / k) * k + arr[nex] + k, nex});
                    }
                }
            }
        }

        long long minres = *sl.rbegin() - *sl.begin();

        vector<unordered_set<long long>> f2(n);
        for (auto& edge : mrr) {
            long long a = edge[0], b = edge[1];
            if (starts[a] + k > starts[b]) {
                f2[b].insert(a);
            }
        }

        for (auto& dropper : droppings) {
            sl.erase(sl.find(starts[dropper.second]));
            starts[dropper.second] -= k;
            sl.insert(starts[dropper.second]);
            vector<long long> stack = {dropper.second};
            while (!stack.empty()) {
                long long cur = stack.back(); stack.pop_back();
                for (long long nex : g[cur]) {
                    if (f2[nex].count(cur) && starts[nex] >= starts[cur] + k) {
                        f2[nex].erase(cur);
                        if (f2[nex].empty()) {
                            sl.erase(sl.find(starts[nex]));
                            starts[nex] -= k;
                            sl.insert(starts[nex]);
                            stack.push_back(nex);
                        }
                    }
                }
            }
            long long res = *sl.rbegin() - *sl.begin();
            minres = min(minres, res);
        }
        cout << minres << endl;
    }
    return 0;
}