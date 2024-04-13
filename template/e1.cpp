#include <iostream>
#include <vector>
#include <cmath>  // Include for pow()

using namespace std;

vector<int> solve_(int n, vector<int>& arr) {
    bool flag = true;
    vector<int> nonzero;
    for (int i = 0; i < n; ++i) {
        nonzero.push_back(i);
    }

    int cnt = static_cast<int>(pow(200000, 0.51));  // Now pow() is recognized
    while (flag && cnt--) {
        flag = false;
        vector<int> next_nonzero;

        for (int idx : nonzero) {
            int cur = idx;
            int next = idx + 1;
            if (cur == n - 1) {
                next = 0;
            }

            if (arr[cur] == 0) continue;
            if (arr[next] > 0) {
                flag = true;
                arr[next] = max(0, arr[next] - arr[cur]);

                if (arr[next] > 0) {
                    next_nonzero.push_back(cur);
                }
            }
        }

        nonzero = next_nonzero;
    }

    for (int i = 0; i < n; ++i) {
        int next = (i + 1) % n;
        if (arr[i] > 0 && arr[next] > 0) {
            arr[next] = 0;
        }
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
    int T;
    cin >> T;
    cin.ignore();  // Ignore the newline after reading T

    for (int case_num = 0; case_num < T; ++case_num) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        vector<int> res = solve_(n, arr);
        cout << res.size() << endl;
        for (size_t i = 0; i < res.size(); ++i) {  // Use size_t to match type with size()
            if (i > 0) cout << " ";
            cout << res[i] + 1;  // Convert zero-based index to one-based
        }
        cout << endl;
    }

    return 0;
}