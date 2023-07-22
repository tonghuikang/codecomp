#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int h, w, n;
    cin >> h >> w >> n;

    vector<vector<int>> mrr(h, vector<int>(w, 0));
    for(int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        mrr[x-1][y-1] = 1;
    }

    vector<vector<int>> arr(h, vector<int>(w, 0));  // right
    vector<vector<int>> brr(h, vector<int>(w, 0));  // down
    vector<vector<int>> crr(h, vector<int>(w, 0));

    for(int i = 0; i < h; i++) {
        int count = 0;
        for(int j = 0; j < w; j++) {
            if(mrr[i][j] == 1) {
                count = 0;
                continue;
            }
            count += 1;
            arr[i][j] = count;
        }
    }

    for(int j = 0; j < w; j++) {
        int count = 0;
        for(int i = 0; i < h; i++) {
            if(mrr[i][j] == 1) {
                count = 0;
                continue;
            }
            count += 1;
            brr[i][j] = count;
        }
    }

    for(int i = 0; i < h; i++) {
        if(mrr[i][0] != 1) {
            crr[i][0] = 1;
        }
    }

    for(int j = 0; j < w; j++) {
        if(mrr[0][j] != 1) {
            crr[0][j] = 1;
        }
    }

    for(int i = 1; i < h; i++) {
        for(int j = 1; j < w; j++) {
            crr[i][j] = min({arr[i][j], brr[i][j], crr[i-1][j-1] + 1});
        }
    }

    long long res = 0;
    for(int i = 0; i < h; i++) {
        for(int j = 0; j < w; j++) {
            res += crr[i][j];
        }
    }

    cout << res << "\n";

    return 0;
}