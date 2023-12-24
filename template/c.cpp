#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

// Fast input reading
int readInt() {
    int x;
    std::cin >> x;
    return x;
}

int solve(int n, int k, int d, std::vector<int>& arr, std::vector<int>& vrr) {
    // grow once and reset, repeat
    int maxres = d / 2;

    // reset and grow once, repeat
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (i + 1 == arr[i]) {
            res += 1;
        }
    }
    res += (d - 1) / 2;
    maxres = std::max(maxres, res);

    // grow multiple, reset, and grow once and reset
    for (int q = 0; q < k; ++q) {
        res = 0;
        for (int i = 0; i < n; ++i) {
            if (i < vrr[q]) {
                arr[i] += 1;
            }
            if (arr[i] == i + 1) {
                res += 1;
            }
        }
        res += (d - q - 1) / 2;
        maxres = std::max(maxres, res);
    }

    return maxres;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t = readInt(); // number of test cases
    while (t--) {
        int n = readInt();
        int k = readInt();
        int d = readInt();
        std::vector<int> arr(n);
        std::vector<int> vrr(k);

        for (int& item : arr) {
            item = readInt();
        }

        for (int& item : vrr) {
            item = readInt();
        }

        int res = solve(n, k, d, arr, vrr);
        std::cout << res << "\n";
    }

    return 0;
}