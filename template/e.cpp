#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> read_matrix(int rows) {
    vector<vector<int>> matrix(rows, vector<int>(2));
    for (int i = 0; i < rows; i++) {
        cin >> matrix[i][0] >> matrix[i][1];
        matrix[i][0]--;  // 0-indexing
        matrix[i][1]--;  // 0-indexing
    }
    return matrix;
}

int solve(int h, int w, int n, vector<vector<int>>& mrr) {
    set<pair<int, int>> mrr_set;
    for (auto& v : mrr) {
        mrr_set.insert({v[0], v[1]});
    }

    vector<vector<int>> arr(h, vector<int>(w, 0));
    vector<vector<int>> brr(h, vector<int>(w, 0));
    vector<vector<int>> crr(h, vector<int>(w, 0));

    for (int i = 0; i < h; i++) {
        int count = 0;
        for (int j = 0; j < w; j++) {
            if (mrr_set.count({i,j}) > 0) {
                count = 0;
                continue;
            }
            count += 1;
            arr[i][j] = count;
        }
    }

    for (int j = 0; j < w; j++) {
        int count = 0;
        for (int i = 0; i < h; i++) {
            if (mrr_set.count({i,j}) > 0) {
                count = 0;
                continue;
            }
            count += 1;
            brr[i][j] = count;
        }
    }

    for (int i = 0; i < h; i++) {
        if (mrr_set.count({i,0}) > 0) {
            continue;
        }
        crr[i][0] = 1;
    }

    for (int j = 0; j < w; j++) {
        if (mrr_set.count({0,j}) > 0) {
            continue;
        }
        crr[0][j] = 1;
    }

    for (int i = 1; i < h; i++) {
        for (int j = 1; j < w; j++) {
            crr[i][j] = min({arr[i][j], brr[i][j], crr[i-1][j-1] + 1});
        }
    }

    int res = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            res += crr[i][j];
        }
    }

    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int h, w, n;
    cin >> h >> w >> n;
    vector<vector<int>> mrr = read_matrix(n);

    int res = solve(h, w, n, mrr);
    cout << res << "\n";

    return 0;
}