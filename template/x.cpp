#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

// ---------------------------- template ends here ----------------------------

bool compute(vector<int>& arr) {
    sort(arr.begin(), arr.end());
    set<int> vals = {0};
    int suffix_size = 0;
    for (int x : arr) {
        suffix_size += x;
    }
    for (int x : arr) {
        suffix_size -= x;
        set<int> new_vals;
        for (int y : vals) {
            if (x + y <= suffix_size) {
                new_vals.insert(x + y);
            }
            if (x + y >= -suffix_size) {
                new_vals.insert(x - y);
            }
        }
        vals = new_vals;
    }
    return vals.count(0) > 0;
}

int query(int pos) {
    cout << pos + 1 << endl;
    cout.flush();
    int response;
    cin >> response;
    return response;
}

// -----------------------------------------------------------------------------

int main() {
    srand(time(0));

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    if (compute(arr)) {
        cout << "Second" << endl;
        cout.flush();
        while (true) {
            int response;
            cin >> response;
            if (response == 0) {
                return 0;
            }
            int idx = response - 1;
            if (arr[idx] == 0) {
                continue;
            }

            vector<int> candidates(n);
            for (int i = 0; i < n; ++i) {
                candidates[i] = i;
            }

            bool found = false;
            for (int pos : candidates) {
                if (pos == idx) {
                    continue;
                }
                if (arr[pos] == 0) {
                    continue;
                }

                int val = min(arr[pos], arr[idx]);
                arr[pos] -= val;
                arr[idx] -= val;

                if (compute(arr)) {
                    cout << pos + 1 << endl;
                    cout.flush();
                    found = true;
                    break;
                }

                arr[pos] += val;
                arr[idx] += val;
            }

            if (!found) {
                break;
            }
        }
    } else {
        cout << "First" << endl;
        cout.flush();
        while (true) {
            int pos = max_element(arr.begin(), arr.end()) - arr.begin();
            int idx = query(pos);
            if (idx == 0) {
                return 0;
            }
            idx -= 1;

            int val = min(arr[pos], arr[idx]);
            arr[pos] -= val;
            arr[idx] -= val;
        }
    }

    return 0;
}