#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    int h, w, n;
    cin >> h >> w >> n;

    set<pair<int, int>> mrr;
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        mrr.insert(make_pair(x - 1, y - 1));
    }

    vector<vector<int>> arr(h, vector<int>(w, 0));
    vector<vector<int>> brr(h, vector<int>(w, 0));
    vector<vector<int>> crr(h, vector<int>(w, 0));

    for (int i = 0; i < h; ++i) {
        int count = 0;
        for (int j = 0; j < w; ++j) {
            if (mrr.count(make_pair(i, j)) > 0) {
                count = 0;
                continue;
            }
            count += 1;
            arr[i][j] = count;
        }
    }

    for (int j = 0; j < w; ++j) {
        int count = 0;
        for (int i = 0; i < h; ++i) {
            if (mrr.count(make_pair(i, j)) > 0) {
                count = 0;
                continue;
            }
            count += 1;
            brr[i][j] = count;
        }
    }

    for (int i = 0; i < h; ++i) {
        if (mrr.count(make_pair(i, 0)) == 0) {
            crr[i][0] = 1;
        }
    }

    for (int j = 0; j < w; ++j) {
        if (mrr.count(make_pair(0, j)) == 0) {
            crr[0][j] = 1;
        }
    }

    for (int i = 1; i < h; ++i) {
        for (int j = 1; j < w; ++j) {
            if (mrr.count(make_pair(i, j)) == 0) {
                crr[i][j] = min(arr[i][j], min(brr[i][j], crr[i - 1][j - 1] + 1));
            }
        }
    }

    long long res = 0;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            res += crr[i][j];
        }
    }

    cout << res << endl;

    return 0;
}