#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solve_(int n, vector<int>& arr) {
    bool flag = true;
    vector<int> nonzero(n);
    for (int i = 0; i < n; ++i) {
        nonzero[i] = i;
    }

    while (flag) {
        flag = false;
        vector<int> nexarr;

        for (int i : nonzero) {
            int cur = i;
            int nex = (i + 1) % n;

            if (arr[cur] == 0) {
                continue;
            }
            if (arr[nex] > 0) {
                flag = true;
                arr[nex] = max(0, arr[nex] - arr[cur]);

                if (arr[nex] > 0) {
                    nexarr.push_back(cur);
                }
            }
        }

        nonzero = std::move(nexarr);
    }

    vector<int> result;
    for (int i = 0; i < n; ++i) {
        if (arr[i] > 0) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int& x : arr) {
            cin >> x;
        }

        vector<int> res = solve_(n, arr);

        cout << res.size() << "\n";
        for (int i = 0; i < res.size(); ++i) {
            if (i > 0) cout << " ";
            cout << res[i] + 1;  // convert 0-based index to 1-based
        }
        cout << "\n";
    }
    return 0;
}